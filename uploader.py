import streamlit as st
import boto3

# AWS 설정
s3 = boto3.client('s3')
BUCKET_NAME = 'ecommerce-video-upload-bucket'

# Streamlit UI
st.title('Admin Video Uploader')

product_id = st.text_input('상품 ID 입력', '')

uploaded_file = st.file_uploader("MP4 파일 업로드", type=['mp4'])

if uploaded_file and product_id:
    if st.button('S3로 업로드'):
        s3.upload_fileobj(
            uploaded_file,
            BUCKET_NAME,
            f'uploads/{product_id}/original.mp4',
            ExtraArgs={'ContentType': 'video/mp4'}
        )
        st.success('업로드 완료!')
