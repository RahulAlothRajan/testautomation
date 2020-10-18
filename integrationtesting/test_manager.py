"""sample test."""


class getthere:
    """This class act as a test manager who performs all integration test of 2getthere deliverables.
    2getther class takes configuration file path as default argument.
    configuration is defined in config.yaml file.
    Attributes
    ----------
    config : str
        path of config.yaml file where all test configurations are defined.

    Methods
    -------
    release_zip_validation(path)
        validate the release zip by extracting and checking the contents are in the correct order or not.
    """

    def __init__(self, config: str):
        self.config = config

    def check_release_zip_extractable(self, root_path: str) -> str():
        """Compares the stable released zip and newly created release zip and -
           returns the differences in file's as a list of variables as a warning to the Product Owner.
        Parameters
        ----------
        root_path : str, root path of the build folder

        return
        ------
        list of differences as file names.
        """
        return str("on_ok")

    def compare_release_zips(self, root_path: str) -> list():
        """Compares the stable released zip and newly created release zip and -
           returns the differences in file's as a list of variables as a warning to the Product Owner.
        Parameters
        ----------
        root_path : str, root path of the build folder

        return
        ------
        list of differences as file names.
        """
        old_release_dir = root_path + "old_release"
        new_release_dir = root_path + "new_release"
        old_release_files = [
            f for f in listdir(root_path) if isfile(join(root_path, f))
        ]
        new_release_files = [
            f for f in listdir(root_path) if isfile(join(root_path, f))
        ]
        return list(set(old_release_files) - set(new_release_files))
