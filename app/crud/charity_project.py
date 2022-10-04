from typing import List, Optional, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectDB


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """Запрос проекта по номеру id"""

        project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> Union[None, List[CharityProjectDB]]:
        """Запрос на все завершённые проекты."""

        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            )
        )
        projects = projects.scalars().all()
        return projects.sort(key=lambda x: x.close_date - x.create_date)


charity_project_crud = CRUDCharityProject(CharityProject)
