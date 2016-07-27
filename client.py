import binascii

fmt='%-30s: %s'

def rever(tar):
    out=[]
    #print tar
    i=0
    while i <len(tar):
        out.append(tar[i:i+2])
        i+=2
    #print out
    out.reverse()
    return (''.join(out)).upper()

def carriage(Name):
    print '-'*50
    print ' '*15, Name, '\n'
    print ' '*7, 'Description', ' '*15, 'Data'
    print '-'*50

def DOS_HEADER(f):
    print fmt %('Signature', rever(binascii.hexlify(f.read(2))))
    print fmt %('Bytes on Last Page of File', rever(binascii.hexlify(f.read(2))))
    print fmt %('Pages in File', rever(binascii.hexlify(f.read(2))))
    print fmt %('Relocations', rever(binascii.hexlify(f.read(2))))
    print fmt %('Size of Header in Paragraphs', rever(binascii.hexlify(f.read(2))))
    print fmt %('Minimum Extra Paragraphs', rever(binascii.hexlify(f.read(2))))
    print fmt %('Maximum Extra Paragraphs', rever(binascii.hexlify(f.read(2))))
    print fmt %('Initial (relatives) SS', rever(binascii.hexlify(f.read(2))))
    print fmt %('Initial SP', rever(binascii.hexlify(f.read(2))))
    print fmt %('Checksum', rever(binascii.hexlify(f.read(2))))
    print fmt %('Initial IP', rever(binascii.hexlify(f.read(2))))
    print fmt %('Initial (relative) CS', rever(binascii.hexlify(f.read(2))))
    print fmt %('Offset to Relocation Table', rever(binascii.hexlify(f.read(2))))
    print fmt %('Overlay Number', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('OEM Identifier', rever(binascii.hexlify(f.read(2))))
    print fmt %('OEM Information', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    print fmt %('Reserved', rever(binascii.hexlify(f.read(2))))
    addr=rever(binascii.hexlify(f.read(4)))
    print fmt %('Offset to New EXE Header', addr)
    return addr

def DOS_STUB(f, end):
    time=int(end, 16)-int('40', 16)
    for i in range(time/16):
        print fmt %('', binascii.hexlify(f.read(16)))
    print fmt %('', binascii.hexlify(f.read(time%16)))

def SIGNATURE(f):
    print fmt %('IMAGE_NT_SIGNATURE', rever(binascii.hexlify(f.read(4))))

def FILE_HEADER(f):
    print fmt %('Machine', rever(binascii.hexlify(f.read(2))))
    num=rever(binascii.hexlify(f.read(2)))
    print fmt %('Number of Sections', num)
    print fmt %('Time Date Stamp', rever(binascii.hexlify(f.read(4))))
    print fmt %('Pointer to Symbol Table', rever(binascii.hexlify(f.read(4))))
    print fmt %('Number of Sumbols', rever(binascii.hexlify(f.read(4))))
    size=rever(binascii.hexlify(f.read(2)))
    print fmt %('Size of Optional Header', size)
    print fmt %('Characteristics', rever(binascii.hexlify(f.read(2))))
    return size, int(num, 16)

def OPTIONAL_HEADER(f, size):
    size=int(size, 16)
    if size<=0:
        return
    print fmt %('Magic', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Major Linker Version', binascii.hexlify(f.read(1)))
    size-=1
    if size<=0:
        return
    print fmt %('Minor Lniker Version', binascii.hexlify(f.read(1)))
    size-=1
    if size<=0:
        return
    print fmt %('Size of Code', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Initialized Data', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Uninitialized Data', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Address of Entry Point', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Base of Code', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Base of Data', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Image Base', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Section Alignment', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('File Alignment', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Major O/S Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Minor O/S Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Major Image Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Minor Image Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Major Subsystem Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Minor Subsystem Version', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Win32 Version Value', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Image', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Headers', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Checksum', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Subsystem', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('DLL Characteristics', rever(binascii.hexlify(f.read(2))))
    size-=2
    if size<=0:
        return
    print fmt %('Size of Stack Reserve', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Stack Commit', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Heap Reserve', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Size of Heap Commit', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Loader Flags', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('Number of Data Directories', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('EXPORT Table RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('EXPORT TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('IMPORT TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('IMPORT TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('RESOURCE TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('RESOURCE TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('EXCEPTION TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('EXCEPTION TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('CERTIFICATE TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('CERTIFICATE TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('BASE RELOCATION TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('BASE RELOCATION TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('DEBUG TABLE RVA', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    print fmt %('DEBUG TABLE Size', rever(binascii.hexlify(f.read(4))))
    size-=4
    if size<=0:
        return
    f.read(size)

def SECTION_HEADER():
    #print fmt %('Name', rever(binascii.hexlify(f.read(4))))
    print fmt %('Virtual Size', rever(binascii.hexlify(f.read(4))))
    print fmt %('RVA', rever(binascii.hexlify(f.read(4))))
    print fmt %('Size of Raw Data', rever(binascii.hexlify(f.read(4))))
    print fmt %('Pointer to Raw Data', rever(binascii.hexlify(f.read(4))))
    print fmt %('Pointer to Relocations', rever(binascii.hexlify(f.read(4))))
    print fmt %('Pointer to Line Numbers', rever(binascii.hexlify(f.read(4))))
    print fmt %('Number of Relocations', rever(binascii.hexlify(f.read(2))))
    print fmt %('Number of Line Numbers', rever(binascii.hexlify(f.read(2))))
    print fmt %('Characteristics', rever(binascii.hexlify(f.read(4))))

def naming(raw):
    raw=binascii.hexlify(raw)
    i=0
    out=[]
    while True:
        if raw[-2:]=='00':
            raw=raw[:-2]
        else:
            while i <len(raw):
                out.append(chr(int(raw[i:i+2], 16)))
                i+=2
            return ''.join(out)

with open(raw_input(), 'rb') as f:
    directories=[]
    carriage('IMAGE_DOS_HEADER')
    STUD_ADDR=DOS_HEADER(f)
    carriage('IMAGE_DOS_STUB')
    DOS_STUB(f, STUD_ADDR)
    carriage('SIGNATURE')
    SIGNATURE(f)
    carriage('IMAGE_FILE_HEADER')
    SIZE_OPT, NUM_DIR=FILE_HEADER(f)
    carriage('IMAGE_OPTIONAL_HEADER')
    OPTIONAL_HEADER(f, SIZE_OPT)
    for i in range(NUM_DIR):
        a=naming(f.read(8))
        carriage('IMAGE_SECTION_HEADER '+a)
        SECTION_HEADER()
    f.seek(int('e8', 16))
    #print rever(binascii.hexlify(f.read(4)))
    #print rever(binascii.hexlify(f.read(2)))