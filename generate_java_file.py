import glob
import os

from generate_repositories.GenerateRepository import GenerateRepository


class Main:

    user_entity_folder = ''
    user_entity_package = ''
    user_repository_folder = ''
    user_repository_package = ''

    exit_option = 0

    print("***************************")
    print("***************************")
    print(" ****Java BackEnd - CLI****")
    print("***************************")
    print("***************************")
    print("\n")
    print("1 - Generate Java Spring Boot Repositories")
    print("0 - Exit")
    print("\n")
    user_choice = int(input('How can I help you ? \n'))

    if(user_choice == 1):
        user_entity_folder = input('Paste the full location of Entities Folder ...\n')
        user_entity_package = input('Paste the package of you entites in the java project ... \n')
        user_repository_folder = input('Repository Destiny Folder ... \n')
        user_repository_package = input('Repository Destiny Package ... \n')
        if((user_entity_folder and user_repository_folder) != None):

            genereate_repository = GenerateRepository()
            genereate_repository.create_repositories(user_entity_folder, user_repository_folder, user_entity_package, user_repository_package)
            print('Done ! Happy Coding ! **) \n')
    elif user_choice == exit_option:
        print("\n")
        print('System End ... **( ')
