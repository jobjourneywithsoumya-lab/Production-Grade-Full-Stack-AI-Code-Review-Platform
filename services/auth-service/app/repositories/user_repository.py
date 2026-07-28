def create_user(
    self,
    name: str,
    email: str,
    hashed_password: str
):
    user = User(
        name=name,
        email=email,
        hashed_password=hashed_password
    )

    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)

    return user