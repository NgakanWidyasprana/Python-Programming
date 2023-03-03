def list(nama):
    list_nama = []
    for domain, body in nama.items():
        for body in body:
            list_nama.append("{}{}".format(body,domain))
    return list_nama

nama = {
    "@gmail.com":["ngakan","ngakan37","william"],
    "@outlook.com":["diah","pramesti","diahpram68"]
}

print(list(nama))
