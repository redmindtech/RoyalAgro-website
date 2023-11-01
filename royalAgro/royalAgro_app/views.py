# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sys
import os
import json
import logging

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import app_util_mail as um

logger = logging.getLogger(settings.LOGGER_FILE_NAME)
# Create your views here.

def index(request):
    fn = "index"
    template_name = "index.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "RoyalAgro International FZE - A Niche Agriculture Commodity Trading Company"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Royal Agro deals with the world’s leading agricultural processors serving our diverse group of customers efficiently and profitably. We operate the one of the world’s distinct and customized crop origination and transportation network, connecting crops in different origins and markets primarily in Asia and elsewhere. "
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
    	pass
    return render(request,template_name, locals())


def about(request):
    fn = "about"
    template_name = "about.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "RoyalAgro International FZE - A Niche Agriculture Commodity Trading Company"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Royal Agro deals with the world’s leading agricultural processors serving our diverse group of customers efficiently and profitably. We operate the one of the world’s distinct and customized crop origination and transportation network, connecting crops in different origins and markets primarily in Asia and elsewhere. "
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
    	pass
    return render(request,template_name, locals())    


def commodities(request):
    fn = "commodities"
    template_name = "commodities.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodities- PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodities, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())   

def resources(request):
    fn = "resources"
    template_name = "resources.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Resources"
        seo_obj['description'] = "Agri Commodity Resources and Reports"
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals()) 

def news(request):
    fn = "news"
    template_name = "news.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "News & Events"
        seo_obj['description'] = "Agri Commodity News and Reports"
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())    

def gallery(request):
    fn = "gallery"
    template_name = "gallery.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Gallery"
        seo_obj['description'] = "Royal Agro Customers"
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())  

def contact(request):
    fn = "contact"
    template_name = "contact.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Contact us"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Royal Agro deals with the world’s leading agricultural processors serving our diverse group of customers efficiently and profitably. We operate the one of the world’s distinct and customized crop origination and transportation network, connecting crops in different origins and markets primarily in Asia and elsewhere. "
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        
        if request.method == "POST":
            p_dict = request.POST.copy()
            print p_dict
            to_emails = settings.ADMIN_EMAIL_USER
            print to_emails
            context = p_dict
            subject_template = "contact_subject.html"
            message_template = "contact_msg.html"
            if to_emails:
                um.sendmail(request, None, to_emails, subject_template, message_template, context)
                return HttpResponseRedirect(reverse("contact_confirmation"))

    except Exception, e:
        logger.info('Error at %s:%s' %(sys.exc_traceback.tb_lineno,e))
    return render(request,template_name, locals()) 

def contact_confirmation(request):
    fn = "contact_confirmation"
    template_name = "contact_confirmation.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Contact Confirmation"
        seo_obj['description'] = "Royal Agro Customers"
        seo_obj["keywords"] = "RoyalAgro International FZE, A Niche Agriculture Commodity Trading Company, PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN, Royal Agro, RAK, Dubai 2020"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())  

def peanuts(request):
    fn = "peanuts"
    template_name = "peanuts.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Peanuts"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, Peanuts, "
        current_page = "peanuts"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())

def greenmungbean(request):
    fn = "greenmungbean"
    template_name = "greenmungbean.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Green Mung Bean"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, Green Mung Bean"
        current_page = "greenmungbean"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals()) 

def coriander(request):
    fn = "coriander"
    template_name = "coriander.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Coriander"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, Coriander"
        current_page = "coriander"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals()) 

def chillies(request):
    fn = "chillies"
    template_name = "chillies.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Chillies"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, chillies"
        current_page = "coriander"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())     

def soybeans(request):
    fn = "soybeans"
    template_name = "soybeans.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Soybeans"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, Soybeans"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())   

def corn(request):
    fn = "corn"
    template_name = "corn.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Agri Commodity - Corn"
        seo_obj['description'] = "RoyalAgro International FZE. A Niche Agriculture Commodity Trading Company. Sources agri commodities like PEANUTS,GREEN MUNG BEAN,CORIANDER,CHILLIES,SOY,CORN from around the world to south asia"
        seo_obj["keywords"] = "Agri Commodity, Corn"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())       

def privacy(request):
    fn = "privacy"
    template_name = "privacy.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Royal Agro Privacy"
        seo_obj['description'] = "Royal Agro Privacy"
        seo_obj["keywords"] = "Royal Agro Privacy"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())

def terms(request):
    fn = "terms"
    template_name = "terms.html"
    
    try:
        seo_obj = dict()
        seo_obj['title'] = "Royal Agro Terms of use"
        seo_obj['description'] = "Royal Agro Terms of use"
        seo_obj["keywords"] = "Royal Agro Terms of use"
        #Banners list
        pass
    except Exception, e:
        pass
    return render(request,template_name, locals())                    


                     