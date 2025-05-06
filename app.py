import streamlit as st

print('page_reloaded')

st.set_page_config(
	page_title='포켓몬 도감',
	page_icon='./images/monsterball.png'
)
st.markdown('''
<style>
img: {
	max-height: 300px;
}
.stExpanderContainer div {
	display: flex;
	justify-content: center;
	font-size: 20px;
}
[data-testid='stElementToolbarButton'] {
	visibility: hidden;
}
</style>
''', unsafe_allow_html=True)

st.title('Streamlit 포켓몬 도감')
st.markdown('**포켓몬**을 하나씩 추가해서 도감을 채워보세요!')

type_emoji_dict = {
    "노말": "NO",
    "격투": "FI",
    "비행": "FL",
    "독": "PO",
    "땅": "GR",
    "바위": "RO",
    "벌레": "BU",
    "고스트": "GH",
    "강철": "ST",
    "불꽃": "FR",
    "물": "WT",
    "풀": "FF",
    "전기": "EL",
    "에스퍼": "ES",
    "얼음": "IC",
    "드래곤": "DR",
    "악": "EV",
    "페어리": "FA"
}


initial_pokemons = [
	{
		"name": "피카츄",
		"types": ["전기"],
		"image_url": "https://i.namu.wiki/i/lJEKaGbGTK0rk8TyLZ-OkGPuL4bT7PuefLHsZhhvbuxXNNaLD5xMhXxP8KEwdUcwKWLTEV6CQKb6KjP4ChmGhawfRnbPcWPwQD86MbGUscWG-LVrPZF9kBGi5W7Q7SiZas_uO7i3Ss_htKF6mE0z0Q.webp"
	},
	{
		"name": "누오",
		"types": ["물", "땅"],
		"image_url": "https://i.namu.wiki/i/72uaYPFteRQDAoSzGhY9-bZH8VWB_bp1iBGH8echat9A6OOLwGG1juHQRrC2xyYC4IZ2FwBKQbF7PCn-u57G5yVomEQ4GajLQ5etCJ8JZqEVDEZMP9K2m6Vv9lXVGQh7BTI0oog37tc127k00sPcxQ.webp"
	},
	{
		"name": "갸라도스",
		"types": ["물", "비행"],
		"image_url": "https://i.namu.wiki/i/skf0eaEikJSoEhoop8ZUd6Jh-Gi0miVBs9t97jdHNO5YXFlt0wTlNIAOa1uFY8JToWiPz9ya30lu9gQj6-Lz2ld05pgact48G5OuMwdWjYcENI7nq0SUJn63C5INQRAH7zut5dDSK-OezjqlQ3yjsA.webp"
	},
	{
		"name": "개굴닌자",
		"types": ["물", "악"],
		"image_url": "https://i.namu.wiki/i/gz57hBo3TXk3PCz38iaEwvZdPXKmIjuKGWAqa9e1bJAGFWWfYhDGVEzp59xUETdt_LTjOCtrBfXkmpHpokcUQuMTCqWJa_0oF1slEEgA2Bz79r97hEWwg5nNHH2wv8bseaozftYytRVGtm7ZQX4BaA.webp"
	},
	{
		"name": "루카리오",
		"types": ["격투", "강철"],
		"image_url": "https://i.namu.wiki/i/mVGWXyZxmZphOSlw0hOyF0B1l9PX_oSwLuzMFDyzU-zMg-RSksMaL6CLiPXaRRvo3JASHekTTKN56thfKxEA84-kbykgRtxCraKfOf7xJXMpcfRKL2lj9oX2cXFE0BrfPuvSfswgEvQBdxW3Mor0MQ.webp"
	},
	{
		"name": "에이스번",
		"types": ["불꽃"],
		"image_url": "https://i.namu.wiki/i/ZFizTfcW6CfktqVx-kndY6neIowgR7kqmZl6M1U535TrE-RZUlmYYBeLHp9J_9m3KJt41FXcFBQf1HBTpL77wzFKiGvgvI7dIJAjQEEHEVZ84Apz4pvAj1iKYImmalyB5ooYudxRj1QmmmeULdOZGA.webp"
	}
]

example_pokemon = {
		"name": "알로라 디그다",
		"types": ["땅", "강철"],
		"image_url": "https://i.namu.wiki/i/v9zD49woIZ-kgSHxr30_dYGSEo_NVvlujouka2Bbf0n53A2TvVxgm792yEi9fKv9Cjqtwr-hrkGrJr8M_wkGJmoOe6ORgSqxkvIR2xP4MVtxJ3sjDOId5b9XoIG8bcD_OGPxECfBISLi91DwaeX35w.webp"
}

if 'pokemons' not in st.session_state:
	st.session_state.pokemons = initial_pokemons


auto_complete = st.toggle('예시 데이터로 채우기')

with st.form(key="form"):
	col1, col2 = st.columns(2)
	with col1:
		name = st.text_input(
					label='포켓몬 이름',
					value=example_pokemon['name'] if auto_complete else ''
		)
	with col2:
		types = st.multiselect(
				label='포켓몬 속성', 
				options=list(type_emoji_dict.keys()),
				max_selections=2,
				default=example_pokemon['types'] if auto_complete else []
		)
	image_url = st.text_input(
					label='포켓몬 이미지 URL',
					value=example_pokemon['image_url'] if auto_complete else ''
		)
	submit = st.form_submit_button(label='Submit')

	if submit:
		if not name:
			st.error('포켓몬의 이름을 입력해주세요.')
		elif len(types) == 0:
			st.error('포켓몬의 속성을 적어도 한개 선택해주세요.')
		else:
			st.success('포켓몬을 추가할 수 있습니다.')

			st.session_state.pokemons.append({
				'name': name,
				'types': types,
				'image_url': image_url if image_url else './images/default.png'
			})


for i in range(0, len(st.session_state.pokemons), 3):
	row_pokemons = st.session_state.pokemons[i:i+3]
	cols = st.columns(3)
	for j in range(len(row_pokemons)):
		with cols[j]:
			pokemon = row_pokemons[j]
			with st.expander(label=f'**{i+j+1}. {pokemon["name"]}**', expanded=True):
				st.image(pokemon["image_url"])
				emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
				st.text(" / ".join(emoji_types))
				delete_button = st.button(label='삭제', key=i+j, use_container_width=True)
				if delete_button:
					print('delete button ckicked!')
					del st.session_state.pokemons[i+j]
					st.rerun()
