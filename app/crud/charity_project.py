from typing import List, Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


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
    ) -> List[CharityProject]:
        """Запрос на все завершённые проекты."""

        projects = await session.execute(
            select([CharityProject.name,
                    CharityProject.description,
                    CharityProject.create_date,
                    CharityProject.close_date]).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(
                extract('year', CharityProject.close_date) -
                extract('year', CharityProject.create_date),
                extract('month', CharityProject.close_date) -
                extract('month', CharityProject.create_date),
                extract('day', CharityProject.close_date) -
                extract('day', CharityProject.create_date),
                extract('hour', CharityProject.close_date) -
                extract('hour', CharityProject.create_date),
                extract('minute', CharityProject.close_date) -
                extract('minute', CharityProject.create_date),
                extract('second', CharityProject.close_date) -
                extract('second', CharityProject.create_date),
            )
        )
        return projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)
