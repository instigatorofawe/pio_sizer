from pathlib import Path


class TreeHandler:
    def __init__(self, input_directories):
        self.input_directories = input_directories
        # Get unique set of .cfr files that exist across all of these directories
        self.cfr_files = [[file.name for file in Path(directory).glob('**/*.cfr')] for directory in input_directories]
        if len(self.cfr_files) > 1:
            unique_cfr_files = set.intersection(*map(set, self.cfr_files))
            self.cfr_files = list(unique_cfr_files)

        # Index for iterator
        self.i = 0

    def __len__(self):
        """
        Number of trees that exist across all input directories
        :return:
        """
        return len(self.cfr_files)

    def __iter__(self):
        """
        Returns an iterator over tuples of trees that exist across all input directories
        :return:
        """
        self.i = 0
        return self

    def __next__(self):
        """
        Returns next element in iterator
        :return: List of paths to cfr files
        """
        if self.i < len(self):
            result = [str(Path(f'%s/%s' % (directory, self.cfr_files[self.i])).resolve()) for directory in self.input_directories]
            self.i += 1
            return result
        else:
            raise StopIteration
