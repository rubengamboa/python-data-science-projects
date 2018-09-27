

    import matplotlib.pyplot as plt
    import wordcloud as wc

    freqs = {"cat": 0.5, "dog":0.4, "fish":0.1}
    wcloud = wc.WordCloud().generate_from_frequencies(freqs)
    plt.imshow(wcloud)
    plt.axis("off")
    plt.savefig("wordcloud.png")