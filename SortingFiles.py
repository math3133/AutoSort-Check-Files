import os, shutil



#remove unwanted directories
def RemoveFolders():
    RemovedFolders = 0
    global Files

    for n in range(len(Files)):

        if os.path.isfile(os.path.join(FilesPath, Files[n - RemovedFolders])) == False:
            del Files[n - RemovedFolders]
            RemovedFolders += 1


def CheckFile(FileName_bis):

    global FilesPath
    global Prefix
    global SM_FileExtensions
    global T_FileExtensions

    ## Check file size if not void
    if (os.path.getsize(os.path.join(FilesPath, FileName_bis))) == 0:
        return " contain nothing, the file size is 0."

    ## Check for unwanted space characters
    elif ' ' in FileName_bis:
        return " contain a space character which need to be removed."
    
    ## Check if there is any Valid Prefix
    for y in range(len(Prefix)):
        if Prefix[y] == FileName_bis[0 : len(Prefix[y])]:
            
            ## Verify file extensions for SM_ prefix 
            if y == 0:
                for x in range(len(SM_FileExtensions)):
                    if SM_FileExtensions[x] == FileName_bis[len(FileName_bis) - (len(SM_FileExtensions[x])) : len(FileName_bis)]:
                        return
                return " contain an invalid or not registered file type."
            
            ## Verify file extension for T_ prefix
            elif y == 1:
                for x in range(len(T_FileExtensions)):
                    if T_FileExtensions[x] == FileName_bis[len(FileName_bis) - (len(T_FileExtensions[x])) : len(FileName_bis)]:
                        return
                return " contain an invalid or not registered file type."

    return " contain no valid prefix."



FilesPath = 'F:\Perso\Python\AutoSort-Check-Files\Files'
OrganisedFilesPath = 'F:\Perso\Python\AutoSort-Check-Files\OrganisedFiles'
Files = os.listdir(FilesPath)

Prefix = ('SM_', 'T_')
SM_FileExtensions = ('.fbx')
T_FileExtensions = ('.png')

RemoveFolders()

for i in range(len(Files)):
    FileName = Files[i]

    Error = CheckFile(FileName)

    if Error == None:

        #remove prefix and suffix to get ObjectName
        FileObject = str(FileName[FileName.index('_') + 1 : len(FileName)])
        if '_' in FileObject:
            FileObject = FileObject[0 : FileObject.index('_')]


        #check if object folder exist and create it if needed
        if os.path.exists(os.path.join(OrganisedFilesPath, FileObject)) == False:
            os.mkdir(os.path.join(OrganisedFilesPath, FileObject))

        #check if object type folder exist and create it if needed
        FilePrefix = str(FileName[0 : FileName.index('_')])
        if FilePrefix == 'SM':
            if os.path.exists(os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs')) == False:
                os.mkdir(os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs'))
        
        elif FilePrefix == 'T':
            if os.path.exists(os.path.join(OrganisedFilesPath, FileObject + '/Textures')) == False:
                os.mkdir(os.path.join(OrganisedFilesPath, FileObject + '/Textures'))

        #move file in folders created
        if FilePrefix == 'SM':
            shutil.move(os.path.join(FilesPath, Files[i]),
                        os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs'))
       
        elif FilePrefix == 'T':    
            shutil.move(os.path.join(FilesPath, Files[i]),
                        os.path.join(OrganisedFilesPath, FileObject + '/Textures'))
    
    else:
        print("The file named " + FileName + Error)