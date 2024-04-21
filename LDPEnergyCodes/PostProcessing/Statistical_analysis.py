from scipy import stats

# Statistical analysis I: one sample/one-tail https://www.reneshbedre.com/blog/ttest.html
# One Sample t - test(single sample t - test) is used for comparing the sample mean (a random sample from a
# population) with the specific value (hypothesized or known mean of the population).In t-test, the population
# variance (σ2) is unknown and it is estimated from the sample variance (s).
def one_sample_test(final_perturbed_data, mean_actual):
    one_stat, one_pval = stats.ttest_1samp(a=final_perturbed_data, popmean=mean_actual)
    return one_stat, one_pval

# Statistical analysis II: paired t-test (bin-wise comparison)
# Performing the paired sample t-test
def paired_t_test(count_actual, counte):
    paired_stat, paired_pval = stats.ttest_rel(count_actual, counte)
    return paired_stat, paired_pval

# Statistical analysis III: Perform Mann-Whitney U testPermalink
# Perform two-sided (yield of two genotypes does not have equal medians) Mann-Whitney U test
def mann_whitney(final_actual_data, final_perturbed_data):
    mw_stat, mw_pval = stats.mannwhitneyu(final_actual_data, final_perturbed_data, alternative="two-sided")
    return mw_stat, mw_pval

def kruskal_wallis_test(final_actual_data, final_perturbed_data):
    kw_stat, kw_pval = stats.kruskal(final_actual_data, final_perturbed_data)
    return kw_stat, kw_pval