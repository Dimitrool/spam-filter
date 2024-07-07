import filter
import quality

if __name__ == "__main__":
    f = filter.MyFilter()
    corpus_dir_train = "/Users/dmitryygalkin/Desktop/git storage/spam filter/spam_filter_dataset/1"
    corpus_dir_test = "/Users/dmitryygalkin/Desktop/git storage/spam filter/spam_filter_dataset/2"
    f.train(corpus_dir_train)
    f.test(corpus_dir_test)
    rate = quality.compute_quality_for_corpus(corpus_dir_test)
    print("Your spam filter has quality %f" % rate)


# paths:
# /Users/dmitryygalkin/Downloads/spam-data-12-s75-h25/1
# /Users/dmitryygalkin/Programming/Python/RPH/HW/Spam_Filter/spam_test
