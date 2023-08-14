import pandas as pd
import numpy as np
from os import path


data_file = path.join(path.dirname(__file__), 'ECT_report_66.xlsx')

Provinces = pd.read_excel(data_file, sheet_name='info_province').set_index('prov_id')

# info_constituency
Constituencies = pd.read_excel(data_file, sheet_name='info_constituency').groupby(
    ['cons_id', 'cons_no', 'prov_id', 'registered_vote', 'total_vote_stations']
).sum().reset_index().set_index('cons_id')

# info_party_overview
Parties = pd.read_excel(
    data_file, sheet_name='info_party_overview', keep_default_na=False,
).rename(columns={'id': 'party_id'}).set_index('party_id')

# Candidate_Constituency
ConstituencyCandidates = pd.read_excel(
    data_file, sheet_name='Candidate_Constituency'
).set_index('mp_app_id')


# Candidate_PartyList
PartyListCandidates = pd.read_excel(data_file, sheet_name='Candidate_PartyList')
PartyListCandidates.index.name = 'id'

# Candidate_PM
PMCandidates = pd.read_excel(data_file, sheet_name='Candidate_PM')
PMCandidates.index.name = 'id'

# result_constituencies_PartyList
PartyListResult = pd.read_excel(
    data_file, sheet_name='result_constituencies_PartyList'
).drop(['party_list_vote_percent'], axis=1)
PartyListResult.index.name = 'id'

# result_constituencies_Candidate
ConstituencyResult = pd.read_excel(
    data_file, sheet_name='result_constituencies_Candidate'
).drop(['mp_app_vote_percent'], axis=1)
ConstituencyResult.index.name = 'id'

# result_constituencies_status
ConstituenciesStatus = pd.read_excel(
    data_file, sheet_name='result_constituencies_status'
).drop([
    'counted_vote_stations', 'percent_count', 'pause_report'
], axis=1)
ConstituenciesStatus.index.name = 'id'

# ref: https://www.bbc.com/thai/articles/c3g79jd8qj1o
_result_summary_data = (
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
MPResult = pd.DataFrame(
    _result_summary_data, columns=['party_id', 'constituencies_count', 'party_list_count']
)
MPResult.index.name = 'id'
