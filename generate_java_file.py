import glob
import os

from generate_repositories.GenerateRepository import GenerateRepository


class Main:

    user_entity_package = ''
    user_repository_package = ''

    # clazzes = []

    # os.chdir("C:/Users/Delano Jr/Documents/Desenvolvimento/Desenvolvimento Python/file-generator/java-classes")
    # for file in glob.glob("*.java"):
    #     clazzes.append(file)

    # print(clazzes)

    # def createClass(files):
    #     for file in files:
    #         file_name = os.path.splitext(os.path.basename(file))
    #         clazz_name = file_name[0] + "Repository"
    #         extension_name = file_name[1]

    #         new_file = open("C:/Users\Delano Jr/Documents/Desenvolvimento/Desenvolvimento Python/file-generator/java-repositories/{file}{extension}".format(
    #             file=clazz_name, extension=extension_name), "w+")
    #         new_file.write("package repository;\n")
    #         new_file.write("import org.classes.{}".format(file_name[0]) + ";")
    #         new_file.write("\n")
    #         new_file.write(
    #             "import org.springframework.data.jpa.repository.JpaRepository;\n")
    #         new_file.write(
    #             "import org.springframework.stereotype.Repository;\n")
    #         new_file.write("\n")
    #         new_file.write("@Repository\n")
    #         new_file.write("public interface {name} extends JpaRepository<{simple_class_name},Long>".format(
    #             name=clazz_name, simple_class_name=file_name[0]) + str('{\n'))
    #         new_file.write(str('}'))
    #         new_file.close()

    # createClass(clazzes)

    print("***************************")
    print("***************************")
    print(" ****Java BackEnd - CLI****")
    print("***************************")
    print("***************************")
    print("\n")
    print("1 - Generate Entities")
    print("\n")
    user_choice = int(input('How can I help you ? \n'))

    if(user_choice == 1):
        user_entity_package = input('Entities Package ...\n')
        user_repository_package = input('Repository Package \n')
        if((user_entity_package and user_repository_package) != None):
            genereate_repository = GenerateRepository()
            genereate_repository.create_repositories(user_entity_package, user_repository_package)
            print('Done ! Happy Coding ! **) ')