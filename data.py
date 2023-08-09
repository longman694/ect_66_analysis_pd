import pandas as pd
import numpy as np
from os import path


data_file = path.join(path.dirname(__file__), 'ECT_report_66.xlsx')

provinces = pd.read_excel(data_file, sheet_name='info_province').set_index('prov_id')

# info_constituency
constituencies = pd.read_excel(data_file, sheet_name='info_constituency').groupby(
    ['cons_id', 'cons_no', 'prov_id', 'registered_vote', 'total_vote_stations']
).sum().reset_index().set_index('cons_id')

# info_party_overview
parties = pd.read_excel(
    data_file, sheet_name='info_party_overview', keep_default_na=False,
).rename(columns={'id': 'party_id'}).set_index('party_id')

# Candidate_Constituency
constituency_candidates = pd.read_excel(
    data_file, sheet_name='Candidate_Constituency'
).set_index('mp_app_id')


# Candidate_PartyList
party_list_candidates = pd.read_excel(data_file, sheet_name='Candidate_PartyList')
party_list_candidates.index.name = 'id'

# Candidate_PM
PM_candidates = pd.read_excel(data_file, sheet_name='Candidate_PM')
PM_candidates.index.name = 'id'

# result_constituencies_PartyList
party_list_result = pd.read_excel(
    data_file, sheet_name='result_constituencies_PartyList'
).drop(['party_list_vote_percent'], axis=1)
party_list_result.index.name = 'id'

# result_constituencies_Candidate
constituency_result = pd.read_excel(
    data_file, sheet_name='result_constituencies_Candidate'
).drop(['mp_app_vote_percent'], axis=1)
constituency_result.index.name = 'id'

# result_constituencies_status
constituencies_status = pd.read_excel(
    data_file, sheet_name='result_constituencies_status'
).drop([
    'counted_vote_stations', 'percent_count', 'pause_report'
], axis=1)
constituencies_status.index.name = 'id'

# ref: https://www.bbc.com/thai/articles/c3g79jd8qj1o
result_summary_data = (
    (726, 112, 39),
    (705, 112, 29),
    (709, 68, 3),
    (743, 39, 1),
    (763, 23, 13),
    (701, 22, 3),
    (707, 9, 1),
    (740, 7, 2),
    (762, 5, 1),
    (773, 2, 0),
    (706, 1, 1),
    (719, 0, 1),
    (712, 0 ,1),
    (778, 0, 1),
    (776, 0, 1),
    (747, 0, 1),
    (761, 0, 1),
    (714, 0, 1),
)
mp_result = pd.DataFrame(
    result_summary_data, columns=['party_id', 'constituencies_count', 'party_list_count']
)
mp_result.index.name = 'id'
