def f(versions):
    versions.sort(key=lambda versions: [int(version)for version in versions.split('.')],
                  reverse=True
                  )
    print(versions)


f(["1.0.1", "2.14.15"])
f(["4.3.11", "4.5.6"])
f(["3.9.5", "4.3.11", "8.1.2", "4.3.6", "4.5.6"])
