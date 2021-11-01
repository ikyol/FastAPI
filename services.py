import shutil
from uuid import uuid4
import aiofiles as aiofiles
from fastapi import UploadFile, BackgroundTasks, HTTPException

from models import Video, User
from schemas import UploadVideo


async def save_video(
        user: User,
        file: UploadFile,
        title: str,
        description: str,
        background_tasks: BackgroundTasks
):
    file_name = f'media/{user.id}_{uuid4()}.mp4'
    if file.content_type == 'video/mp4':
        background_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail='It is not mp4')
    info = UploadVideo(title=title, description=description)
    return await Video.objects.create(file=file_name, user=user, **info.dict())


def write_video(file_name: str, file: UploadFile):
    # async with aiofiles.open(file_name, 'wb') as buffer:
    #     data = await file.read()
    #     await file.write(data)
    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
