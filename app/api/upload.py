from werkzeug.utils import secure_filename
import os
import pefile
import pyexifinfo as p
import subprocess

trid_path = "/home/yskim/webdir/trid/trid"

def file_upload(request, upload_folder):
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        file.save(os.path.join(filepath))

        pejson = file_analysis(filepath)


        return pejson


def trid(filepath):
    proc = subprocess.Popen([trid_path, filepath], stdout=subprocess.PIPE)
    cnt = 0
    trids = []
    for line in proc.stdout:
        cnt += 1
        if cnt > 6:
            trid = {}
            line = line.rstrip().lstrip().split()
            percent = line[0]
            ftype = line[1].rstrip(b')').lstrip(b'(.')
            desc = b" ".join(line[2:-1])
            trid['percent'] = percent.decode()
            trid['ftype'] = ftype.decode()
            trid['desc'] = desc.decode()
            trids.append(trid)
    return trids

def file_analysis(filepath):
    p.ver()
    py = p.get_json(filepath)[0]
    try:
        pe = pefile.PE(filepath)
    except pefile.PEFormatError:
        pass
    pejson = {}
    try:
        pejson["Filename"] = py["File:FileName"]
    except:
        pass
    try:
        pejson["FileType"] = py["File:FileType"]
    except:
        pass
    try:
        pejson["FileSize"] = py["File:FileSize"]
    except:
        pass
    try:
        pejson["MIMEType"] = py["File:MIMEType"]
    except:
        pass
    try:
        pejson["Entropy"] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    except:
        pass
    try:
        pejson["ImageVersion"] = py["EXE:ImageVersion"]
    except:
        pass
    try:
        pejson["LinkerVersion"] = py["EXE:LinkerVersion"]
    except:
        pass
    try:
        pejson["MachineType"] = py["EXE:MachineType"]
    except:
        pass
    try:
        pejson["CPUArchitecture"] = py["EXE:CPUArchitecture"]
    except:
        pass
    try:
        pejson["CPUByteOrder"] = py["EXE:CPUByteOrder"]
    except:
        pass
    try:
        pejson["CPUType"] = py["EXE:CPUType"]
    except:
        pass
    try:
        pejson["ObjectFileType"] = py["ObjectFileType"]
    except:
        pass
    try:
        pejson["PEType"] = py["EXE:PEType"]
    except:
        pass
    try:
        pejson["Subsystem"] = py["EXE:Subsystem"]
    except:
        pass
    try:
        pejson["TimeStamp"] = py["EXE:TimeStamp"]
    except:
        pass

    #pejson["Trid"] = trid(filepath)

    return pejson

