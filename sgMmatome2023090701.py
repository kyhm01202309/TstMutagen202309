"""WMAファイルなど対象ファイル以外を移動するのはOK!
今後は。基本方針の1－2から行う。MP３MP４AACをアルバムに振り分けるところから。"""


from pathlib import Path
import shutil
import os
import sys
import glob
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
import datetime

MmatomeMoto01 = 'C:/Users/bakab/Music/tstPyBunrui/tstKankyo/MmatomeMoto01/'
MmatomeIdo01 = 'C:/Users/bakab/Music/tstPyBunrui/MmatomeIdo01/'
MmatomeHoka01 = 'C:/Users/bakab/Music/tstPyBunrui/Mmatomehoka01/'

logMmatome = open('logMmatome.txt', 'w', encoding='UTF-8')
FlNamCSV01 =  open('FlNamCSV0101.csv', 'w', encoding='UTF-8')
logMmatome = open('logMmatome.txt', 'a', encoding='UTF-8')

"change systemchar to blank"
"""def seikeiNam(oMotoNam):
    oShinNam = oMotoNam.replace('\\u3000', '').replace(
        '[', '').replace(']', '').replace('\\', '') \
        .replace('\'', '').replace('\"', '')\
        .replace('x00', '').replace('/', '')\
        .replace(':', '').replace(',', '')\
        .replace('?', '').replace('!', '')\
        .replace('～', '').replace('.', '')\
        .replace('<', '').replace('>', '')
    oShinNam2 = oShinNam.strip()
    return oShinNam2
"""

"subroutine1"
def csvKiroku01(flFllPathUke):
    titleNam1="aaa111"
    traNum1=999
    albNam1=""
    encBy1=""
    strflFllPathUke = str(flFllPathUke)
    "dir or not dir judge "
    if not os.path.isdir(flFllPathUke):
        if ".m4a" in strflFllPathUke or".mp4" in strflFllPathUke or".mp3" in strflFllPathUke:
            try:
                if ".m4a" in strflFllPathUke:
                    muTg= MP4(strflFllPathUke)
                    titleNam1 = muTg["\xa9nam"][0]
                    albNam1 = muTg["\xa9alb"][0]
                    traNum1 = muTg["trkn"][0][0]
                    encBy1 = "m4a"
                elif ".mp4" in strflFllPathUke:
                    muTg= MP4(strflFllPathUke)
                    titleNam1 = muTg["\xa9nam"][0]
                    albNam1 = muTg["\xa9alb"][0]
                    traNum1 = muTg["trkn"][0][0]
                    encBy1 = "mp4"
                elif ".mp3" in strflFllPathUke:
                    muMP3 = MP3(strflFllPathUke)
                    muTg = muMP3.tags
                    titleNam1 = format(muTg.get('TIT2', 'No title'))
                    albNam1 = format(muTg.get('TALB', 'No album title'))
                    traNum1 = format(muTg.get('TRCK',9999))
                    encBy1 = "mp3"
                else:
                    logMmatome.write("04 "+strflFllPathUke+" >>NAME GET FAILED01."+" \n")
                    sys.exit()
            except:
                logMmatome.write("05 "+strflFllPathUke+" >>NAME GET FAILED02."+" \n")
                sys.exit()
            else:
                logMmatome.write("06 "+strflFllPathUke+' TRY TO ALBUM INFO '+" \n")
                try:
                    logMmatome.write("07 TITLE=>>"+titleNam1+"    TRANUM=>>"+str(traNum1)+"    ALBNAM=>>"+albNam1+"   encBy1>>"+encBy1+"\n")
                except:
                    logMmatome.write("08 MUSICTAG GET ROUTINE FAILED. EXIT.>>    "+strflFllPathUke+'is to HokaPath!'+" \n")
                    "shutil.move(flFllPathUke,MmatomeHoka01)"
                    sys.exit()
        else:
            try:
                logMmatome.write("10"+strflFllPathUke+' IS NOT MuFile.'+" \n")
                shutil.move(flFllPathUke,MmatomeHoka01)
            except:
                try:
                    cpNow = datetime.datetime.now
                    cpNowPlus = f'{cpNow: %Y%m%d}'
                    flFllPathUke2 = flFllPathUke+cpNowPlus
                    os.rename(flFllPathUke,flFllPathUke2)
                    shutil.move(flFllPathUke2,MmatomeHoka01)
                except:
                    os.rename(flFllPathUke2,flFllPathUke)
                    logMmatome.write("12"+str(flFllPathUke)+' is SOMETHING BAD. ROUTINE STOP  \n')
                    sys.exit()                    
    else:
        logMmatome.write("16"+strflFllPathUke+' IS DIR.'+" \n")

"main routine"
"seeking folder 1st layer"
p=MmatomeMoto01+"*"
pList = glob.glob(p)
for pGyouBango in pList:
    logMmatome.write("01 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    print("01 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    csvKiroku01(pGyouBango)
    logMmatome.write("20 ONE-STEP END \n\n")
    print("20 ONE-STEP END \n\n")
"seeking foulder 2nd layer"
p=MmatomeMoto01+"**/*"
pList = glob.glob(p)
for pGyouBango in pList:
    logMmatome.write("001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    print("001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    csvKiroku01(pGyouBango)
    logMmatome.write("200 ONE-STEP END \n\n")
    print("200 ONE-STEP END \n\n")
"seeking folder 3rd layer"
p=MmatomeMoto01+"**/**/*"
pList = glob.glob(p)
for pGyouBango in pList:
    logMmatome.write("0001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    print("0001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    csvKiroku01(pGyouBango)
    logMmatome.write("2000 ONE-STEP END \n\n")
    print("2000 ONE-STEP END \n\n")
"seeking folder 4th layer,perhaps not exist"
p=MmatomeMoto01+"**/**/**/*"
pList = glob.glob(p)
for pGyouBango in pList:
    logMmatome.write("00001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    print("00001 pGYOUBANGO>>  "+str(pGyouBango)+" \n")
    csvKiroku01(pGyouBango)
    logMmatome.write("20000 ONE-STEP END \n\n")
    print("20000 ONE-STEP END \n\n")
logMmatome.write("90000 ALL-END \n")
print("90000 ALL-END \n")




"under here, these are component command for coding. basically not part of code."
"""
    mIdoPath = mKbtsPath+seikeiAlbNam
    if not os.path.exists(mIdoPath):
        os.mkdir(mIdoPath)
    try:
        logBri.write(flFllPathUke+'is good routine!')
        shutil.move(flFllPathUke,mIdoPath)
        logBri.write(flFllPathUke+'is tomHokaPath routine!')
    except:
        shutil.move(flFllPathUke,mHokaPath)
        return
"""


"""    for fl1 in fls1:
        shoriNO = shoriNO+1 
        print('shoriNO='+str(shoriNO)+', fl1='+fl1)
        logIdo.write('shoriNO='+str(shoriNO)+', fl1='+fl1)
        if os.path.isdir(fl1):
            print(fl1+' is DIR DESU.')
            logIdo.write(fl1+' is DIR DESU.')
        else:
            fl1Nam = os.path.basename(fl1)
            if os.path.exists(muIdoPath+fl1Nam) or os.path.exists(muIdoHokaPath+fl1Nam):
                logIdo.write('\n\n=========CAUTION!!'+fl1+'is SUDENIARU')
            elif '.jpg'in fl1Nam or'.ini'in fl1Nam or'.db'in fl1Nam:
                os.remove(fl1)
                logIdo.write('\n\n=========CAUTION!!'+fl1+'is REMOVED!!!')
            elif '.m4a'in fl1Nam or '.mp3'in fl1Nam:
                shutil.move(fl1,muIdoPath)
                logIdo.write('\n'+fl1+'is muIdoPath!!!')
            else:
                shutil.move(fl1,muIdoHokaPath)
                logIdo.write('\n'+fl1+'is muIdoHokaPath!!!')
    flsNo1 = flsNo1+1
print('sg1 ALL OPERATION DONE')
logIdo.write('sg1 ALL OPERATION DONE')
"""


"""
def albIdo(muKataUke,flFllPathUke):
    if muKataUke=='.m4a'or'.mp4':
        muTgF1 = EasyMP4(flFllPathUke)
    elif muKataUke=='.mp3':
        muTgF1 = EasyID3(flFllPathUke)
    else:
        logBri.write(flFllPathUke+'is tomHokaPath routine!')
        shutil.move(flFllPathUke,mHokaPath)
        return
    try:
        albNam1 = str(muTgF1["album"])
    except:
        logBri.write(flFllPathUke+'is tomHokaPath routine!')
        shutil.move(flFllPathUke,mHokaPath)
        return
    seikeiAlbNam = seikeiNam(albNam1)
    mIdoPath = mKbtsPath+seikeiAlbNam
    if not os.path.exists(mIdoPath):
        os.mkdir(mIdoPath)
    try:
        logBri.write(flFllPathUke+'is good routine!')
        shutil.move(flFllPathUke,mIdoPath)
    except:
        logBri.write(flFllPathUke+'is tomHokaPath routine!')
        shutil.move(flFllPathUke,mHokaPath)
        return
"""



"""try:
                    csvStrFullPath = str(flFllPathUke)
                    csvTitleNam = titleNam1
                    csvTrackNum = traNum1
                    csvAlbNam = albNam1
                    csvEncby = encdBy1
                    csvBunruiSaki = "999999"
                    csvIdoChk = 0
                    CSVPATH= "FlNamCSV0101.csv"
                    LnNamCSV01=list(range(7))
                    LnNamCSV01=[[csvStrFullPath],[csvTitleNam],[csvTrackNum],[csvAlbNam],[csvEncby],[csvBunruiSaki],[csvIdoChk]]
                    with open(CSVPATH,mode="a",encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerows(LnNamCSV01)
                except:
                    logMmatome.write('MUSICCSV WRITE SUB FAILED.PROCESS EXIT.>>    '+strflFllPathUke+'is to HokaPath!')
                    shutil.move(flFllPathUke,MmatomeHoka01)
                    sys.exit()  
"""