import utils
import confmat

def quality_score(tp, tn, fp, fn):
    score = (tp + tn)/(tp + tn + 10*fp + fn)
    return score
    
def compute_quality_for_corpus(corpus_dir):
    file_name = corpus_dir + "/" + "!truth.txt"
    truth_dict = utils.read_classification_from_file(file_name)
    file_name = corpus_dir + "/" + "!prediction.txt"
    pred_dict = utils.read_classification_from_file(file_name)
    matrix = confmat.BinaryConfusionMatrix("SPAM", "OK")
    matrix.compute_from_dicts(truth_dict, pred_dict)
    quality = quality_score(matrix.tp, matrix.tn, matrix.fp, matrix.fn)
    return quality


