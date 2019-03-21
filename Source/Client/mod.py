class Version():
    def __init__(self, version : list):
        self._version = version

    def __str__(self):
        return '.'.join(self._version)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._version == other._version

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError

        for this, that in zip(self._version, other._version):
            if this > that:#    this is greater
                return True
            if this < that:#    that is greater
                return False
        return False#   they're equal

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError

        for this, that in zip(self._version, other._version):
            if this < that:#    this is less
                return True
            if this > that:#    that is less
                return False
        return False#   they're equal

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

class ModDependency():
    def __init__(self, modName : str, minimumVersion : list, maximumVersion : list):
        self.modName = modName
        self.minimumVersion = Version(minimumVersion)
        self.maximumVersion = maximumVersion

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.modName == other.modName and self.minimumVersion == other.minimumVersion and self.maximumVersion == other.maximumVersion

    def Merge(self, other):
        if self.modName != other.modName:
            raise ValueError("Cannot merge two different mods")
        if self.minimumVersion > other.maximumVersion or self.maximumVersion < other.minimumVersion:
            raise ValueError("Incompatible mod dependencies")
        return ModDependency(self.modName, max([self.minimumVersion, other.minimumVersion]), min([self.maximumVersion, other.maximumVersion]))

        