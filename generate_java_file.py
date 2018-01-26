import glob,os

class Main:
    
    clazzes = []

    os.chdir("C:/Users/delano.duarte/Documents/Ambiente Desenvolvimento/workspaceMars/java-backend-cli/src/org/classes")
    for file in glob.glob("*.java"):
        clazzes.append(file)
    
    print(clazzes)

    def createClass(files):
        for file in files:
            file_name = os.path.splitext(os.path.basename(file))
            clazz_name = file_name[0] + "Repository"
            extension_name = file_name[1]

            new_file = open("C:/Users/delano.duarte/Documents/Ambiente Desenvolvimento/workspaceMars/java-backend-cli/src/repository/{file}{extension}".format(file=clazz_name,extension=extension_name),"w+")
            new_file.write("package repository;\n")
            new_file.write("import org.classes.{}".format(file_name[0])+";")
            new_file.write("\n")
            new_file.write("import org.springframework.data.jpa.repository.JpaRepository;\n")
            new_file.write("import org.springframework.stereotype.Repository;\n")
            new_file.write("\n")
            new_file.write("@Repository\n")
            new_file.write("public interface {name} extends JpaRepository<{simple_class_name},Long>".format(name=clazz_name,simple_class_name=file_name[0]) + str('{\n'))
            new_file.write(str('}'))
            new_file.close()
    
    createClass(clazzes)
