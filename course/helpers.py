import uuid

class SaveMediaFiles(object):
    def save_course_image(instance, filename):
        image_path = filename.split(".")[-1]
        return f"course/course/{uuid.uuid4()}.{image_path}"