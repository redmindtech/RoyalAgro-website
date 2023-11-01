# -*- coding: utf-8 -*-

# From python
import sys
import logging
import threading

# From Django
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.core import mail
from django.conf import settings


logger = logging.getLogger(settings.LOGGER_FILE_NAME)


def sendmail(request, from_email, to_emails, subject_template, message_template, context):
    """
    Api to send emails to users.
       args:
           request : the input request.
           from_email : from user email id. default value is 'None'
           to_emails : list of receivers email ids
           subject_template : mail subject (.html file path)
           message_template : mail content file(.html file path)
           context : dictionary of values to be included in the mail content
    """
    
    fn=sys._getframe(1).f_code.co_name
    logger.info("{0} method is loading....".format(fn))
    try:
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL
        try:
            subject = render_to_string(subject_template, context, context_instance = RequestContext(request))
        except:
            subject = render_to_string(subject_template, context)
        subject = "".join(subject.splitlines())
        try:
            message = render_to_string(message_template, context, context_instance = RequestContext(request))
        except:
            message = render_to_string(message_template, context)

        #call mail thread
        mailThread = MailThread("USERS",subject,message,from_email,to_emails)
        mailThread.setDaemon(False)
        logger.info("starting MailThread: {0}".format(mailThread.name))
        mailThread.start()
    except Exception,e:
        logger.info('Error at %s:%s' %(sys.exc_traceback.tb_lineno,e))
    logger.info("{0} method is loading done....".format(fn))


def sendmail_to_managers(request,subject_template,message_template,context):
    """
    Api to send emails to managers.
       args:
           request : the input request.
           subject_template : mail subject (.html file path)
           message_template : mail content file(.html file path)
           context : dictionary of values to be included in the mail content
    """
    fn=sys._getframe(1).f_code.co_name
    logger.info("{0} method is loading....".format(fn))
    try:
        try:
            subject = render_to_string(subject_template, context, context_instance = RequestContext(request))
        except:
            subject = render_to_string(subject_template, context)
        subject = "".join(subject.splitlines())

        try:
            message = render_to_string(message_template, context, context_instance = RequestContext(request))
        except:
            message = render_to_string(message_template, context)
        
        #call mail thread
        mailThread = MailThread("ADMIN",subject,message,"","")
        mailThread.setDaemon(False)
        logger.info("starting MailThread: {0}".format(mailThread.name))
        mailThread.start()

    except Exception, e:
        logger.info('Error at %s:%s' %(sys.exc_traceback.tb_lineno,e))
    logger.info("{0} method is loading done....".format(fn))


class MailThread(threading.Thread):
    """
    Mail Thred function, useful for sending multiple emails simultaneously

    """

    def __init__(self, to_whom,subject,message,from_user,to_user_list):
        threading.Thread.__init__(self)
        self.to_whom      = to_whom
        self.subject      = subject
        self.message      = message
        self.from_user    = from_user
        self.to_users     = to_user_list


    def run(self):
        try:
            
            if self.to_whom == "ADMIN":
                mail.mail_managers(self.subject, self.message)
            else:
                logger.info("Email Id : {0}".format(self.to_users))
                msg = EmailMultiAlternatives(self.subject, self.message, self.from_user,self.to_users)
                msg.attach_alternative(self.message, "text/html")
                msg.send(fail_silently=False)
        except Exception, e:
            logger.info('Error at %s:%s' %(sys.exc_traceback.tb_lineno,e))
