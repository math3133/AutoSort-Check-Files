import os, shutil


## Remove unwanted directories
def RemoveFolders(FilesPath_bis):
    RemovedFolders = 0
    global Files

    for n in range(len(Files)):

        if os.path.isfile(os.path.join(FilesPath_bis, Files[n - RemovedFolders])) == False:
            del Files[n - RemovedFolders]
            RemovedFolders += 1


def CheckFile(FileName_bis, FilesPath_bis):

    global Prefix
    global SM_FileExtensions
    global T_FileExtensions


    ## Check file size if not void
    if (os.path.getsize(os.path.join(FilesPath_bis, FileName_bis))) == 0:
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

def main(FilesPath : str, OrganisedFilesPath : str) -> None:

    global Files
    global Prefix
    global SM_FileExtensions
    global T_FileExtensions

    Files = os.listdir(FilesPath)

    Prefix  = ('SM_', 'T_')
    SM_FileExtensions  = ('.fbx')
    T_FileExtensions = ('.png')

    logs = []

    RemoveFolders(FilesPath)

    for i in range(len(Files)):
        FileName = Files[i]

        Error = CheckFile(FileName, FilesPath)

        if Error == None:

            ## Remove prefix to get Object Name
            FileObject = str(FileName[FileName.index('_') + 1 : len(FileName)])
        
            ## Remove extension
            FileObject = str(FileObject[0 : FileObject.index('.')])
        
            ## Remove suffix if there is any
            if '_' in FileObject:
                FileObject = FileObject[0 : FileObject.index('_')]


            ## Check if object folder exist and create it if needed
            if os.path.exists(os.path.join(OrganisedFilesPath, FileObject)) == False:
                os.mkdir(os.path.join(OrganisedFilesPath, FileObject))

            ## Check if object type folder exist and create it if needed
            FilePrefix = str(FileName[0 : FileName.index('_')])
            if FilePrefix == 'SM':
                if os.path.exists(os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs')) == False:
                    os.mkdir(os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs'))
        
            elif FilePrefix == 'T':
                if os.path.exists(os.path.join(OrganisedFilesPath, FileObject + '/Textures')) == False:
                    os.mkdir(os.path.join(OrganisedFilesPath, FileObject + '/Textures'))

            ## Move file in folders created
            if FilePrefix == 'SM':
                shutil.move(os.path.join(FilesPath, Files[i]),
                            os.path.join(OrganisedFilesPath, FileObject + '/StaticMeshs'))
       
            elif FilePrefix == 'T':    
                shutil.move(os.path.join(FilesPath, Files[i]),
                            os.path.join(OrganisedFilesPath, FileObject + '/Textures'))
    
        else:
            logs.append("The file named " + FileName + Error)
    
    logs.append("----Execution Ended----")
    return logs