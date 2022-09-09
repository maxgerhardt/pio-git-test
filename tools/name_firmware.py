Import("env")

my_flags = env.ParseFlags(env['BUILD_FLAGS'])
defines = dict()
for x in my_flags.get("CPPDEFINES"):
    if type(x) is tuple:
        (k,v) = x
        defines[k] = v
    else:
        defines[x] = "" # empty value
# defines.get("PIO_SRC_TAG") - tag name
env.Replace(
    PROGNAME="%s-%s-%s-%s-%s" %
    (defines.get("PIO_SRC_NAM"), defines.get("VERSION"), str(env["BOARD"]),
     defines.get("PIO_SRC_REV"), defines.get("PIO_SRC_BRH")))