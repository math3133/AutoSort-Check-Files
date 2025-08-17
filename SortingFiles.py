import os, shutil

# Check name files
def CheckFilesName(file):

    global FileNameValid

    try :
        if '_' in file :
            FileNameValid = True
    except :
        FileNameValid = False

#remove unwanted directories
def RemoveFolders():
    RemovedFolders = 0
    global Files

    for i in range(len(Files) - 1):

        if os.path.isfile(os.path.join(FilesPath, Files[i - RemovedFolders])) == False:
            del Files[i - RemovedFolders]
            RemovedFolders += 1




FilesPath = 'F:/Perso/Python/SortingFiles/Files'
OrganisedFilesPath = 'F:/Perso/Python/SortingFiles/OrganisedFiles'
Files = os.listdir(FilesPath)
FileNameValid = False


RemoveFolders()

for i in range(len(Files)):
    FileName = Files[i]

    CheckFilesName(FileName)

    if FileNameValid == True:

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
        print(FileName + " file, contains an error in it's name.")