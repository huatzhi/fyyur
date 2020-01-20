import enum


class Genre(enum.Enum):
    ALTERNATIVE = "Alternative"
    BLUES = "Blues"
    CLASSICAL = "Classical"
    COUNTRY = "Country"
    ELECTRONIC = "Electronic"
    FOLK = "Folk"
    FUNK = "Funk"
    HIP_HOP = "Hip-Hop"
    HEAVY_METAL = "Heavy Metal"
    INSTRUMENTAL = "Instrumental"
    JAZZ = "Jazz"
    MUSICAL_THEATRE = "Musical Theatre"
    POP = "Pop"
    PUNK = "Punk"
    R_N_B = "R&B"
    REGGAE = "Reggae"
    ROCK_N_ROLL = "Rock n Roll"
    SOUL = "Soul"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(choice, choice) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)
