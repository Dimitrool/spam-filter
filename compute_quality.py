import filter
import quality

if __name__ == "__main__":
    f = filter.MyFilter()
    corpus_dir_train = "path to training data"
    corpus_dir_test = "path to testing data"
    f.train(corpus_dir_train)
    f.test(corpus_dir_test)
    rate = quality.compute_quality_for_corpus(corpus_dir_test)
    print("Your spam filter has quality %f" % rate)
