import glob
import os


class GenerateRepository:

    def create_repositories(self, entity_path, repository_path):

        entity_classes = self.search_entities_on_package(entity_path)

        for file in entity_classes:
            file_name = os.path.splitext(os.path.basename(file))
            clazz_name = file_name[0] + "Repository"
            extension_name = file_name[1]

            new_file = open(repository_path + "\{file}{extension}".format(
                file=clazz_name, extension=extension_name), "w+")

            new_file.write("package repository;\n")
            new_file.write("import org.classes.{}".format(file_name[0]) + ";")
            new_file.write("\n")
            new_file.write(
                "import org.springframework.data.jpa.repository.JpaRepository;\n")
            new_file.write(
                "import org.springframework.stereotype.Repository;\n")
            new_file.write("\n")
            new_file.write("@Repository\n")
            new_file.write("public interface {name} extends JpaRepository<{simple_class_name}, Long>".format(
                name=clazz_name, simple_class_name=file_name[0]) + str('{\n'))
            new_file.write(str('}'))
            new_file.close()

    def search_entities_on_package(self, entities_path):
        entities = []
        os.chdir(entities_path)
        for file in glob.glob("*.java"):
            entities.append(file)
            print(file)
        return entities
