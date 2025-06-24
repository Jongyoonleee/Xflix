st.header('Xflix by Someone Else')
import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '98c603bd023b686eb1d668f20d237042'
tmdb.language = 'ko-KR'

def get_recommendations(title):
    #영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = movies[movies['title'] ==title].index[0]

    #코사인 유사도 매트릭스 (cosine_sim)에서 idx에 해당하는 데이터를 (idx, 유사도)형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    #코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
    
    #자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11] 

    #추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]

    #인덱스 정보를 통해 영화 제목 추출
    images=[]
    titles=[]
    for i in movie_indices:
       id =  movies['id'].iloc[i]
       details = movie.details(id)

       image_path = details['poster_path']
       if image_path:
           image_path = 'http://image.tmdb.org/t/p/w500' + image_path
       else:
           image_path = 'no_image.jpg'
       
           
       
       images.append(image_path)
       titles.append(details['title'])

    return images, titles

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout = 'wide')
st.header('Xflix - Movie Recommendation Service')
# Add tabs
tab1, tab2 = st.tabs(["📽️ 영화 추천", "ℹ️ 이 웹사이트는?"])

with tab2:
    st.subheader("Xflix에 오신 것을 환영합니다!")
    st.write("""
    **Xflix**는 사용자가 선택한 영화와 유사한 영화를 추천해주는 웹사이트입니다.
    
    - 인공지능 기반의 **코사인 유사도(Cosine Similarity)** 기법을 사용하여 추천합니다.
    - TMDb API를 통해 영화 포스터와 정보를 가져옵니다.
    - 현재는 10개의 추천 영화를 제공합니다.

    🎯 원하는 영화를 선택하고 'Recommend' 버튼을 눌러보세요!
    """)
















movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like', movie_list)
if st.button('Recommend'):
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0,2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1 
import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '98c603bd023b686eb1d668f20d237042'
tmdb.language = 'ko-KR'

def get_recommendations(title):
    #영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = movies[movies['title'] ==title].index[0]

    #코사인 유사도 매트릭스 (cosine_sim)에서 idx에 해당하는 데이터를 (idx, 유사도)형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    #코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
    
    #자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11] 

    #추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]

    #인덱스 정보를 통해 영화 제목 추출
    images=[]
    titles=[]
    for i in movie_indices:
       id =  movies['id'].iloc[i]
       details = movie.details(id)

       image_path = details['poster_path']
       if image_path:
           image_path = 'http://image.tmdb.org/t/p/w500' + image_path
       else:
           image_path = 'no_image.jpg'
       
           
       
       images.append(image_path)
       titles.append(details['title'])

    return images, titles

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout = 'wide')
st.header('Xflix - Movie Recommendation Service')
# Add tabs
tab1, tab2 = st.tabs(["📽️ 영화 추천", "ℹ️ 이 웹사이트는?"])

with tab2:
    st.subheader("Xflix에 오신 것을 환영합니다!")
    st.write("""
    **Xflix**는 사용자가 선택한 영화와 유사한 영화를 추천해주는 웹사이트입니다.
    
    - 인공지능 기반의 **코사인 유사도(Cosine Similarity)** 기법을 사용하여 추천합니다.
    - TMDb API를 통해 영화 포스터와 정보를 가져옵니다.
    - 현재는 10개의 추천 영화를 제공합니다.

    🎯 원하는 영화를 선택하고 'Recommend' 버튼을 눌러보세요!
    """)
















movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like', movie_list)
if st.button('Recommend'):
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0,2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1 
>>>>>>> d00e6bb (Initial commit of Xflix project)
