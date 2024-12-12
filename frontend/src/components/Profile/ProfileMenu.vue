<template>
  <div id="menu">
    <div id="staff">
      <div class="profile">
        <img
          class="profile-photo"
          src="@/../static/images/profile-no-photo.jpeg"
          alt="Profile photo"
        />
        <h3 class="profile-name">Миколяй Антон Дмитриевич</h3>
      </div>
      <ul class="staff-data">
        <ul class="staff-field">
          <b class="staff-field-name">Должность:</b>
          Библиотекарь
        </ul>
        <ul class="staff-field">
          <b class="staff-field-name">Номер телефона:</b>
          +7 (963) 650-42-93
        </ul>
        <ul class="staff-field">
          <b class="staff-field-name">Рабочая почта:</b>
          pochta@mail.ru
        </ul>
      </ul>
    </div>
    <router-link :to="{ name: 'admin' }" class="button"
      >Управление сотрудниками</router-link
    >
  </div>
</template>

<style lang="sass" scoped>
#menu {
    display: flex;
    flex-direction: column;
	width: 100%;
	max-width: 32em;

    justify-content: space-between;

    background-color: white;
    color: #6699CC;
    padding: 1.5em 3.75em;
}

.profile-name,
.staff-field-name {
    color: #5076B6;
    font-variation-settings: "wght" 600;
	font-weight: 600;
}

.profile {
    display: flex;
    direction: row;

    gap: 1.6em;
    justify-content: center;
    align-items: center;
    position: relative;
}

.profile-photo {
    width: 100%;
    height: 100%;
    max-width: 7.5em;
    min-width: 7.5em;
    max-height: 7.5em;
    aspect-ratio: 1 / 1;
    object-fit: cover;

    border: 3px solid #5076B6;
    border-radius: 50%;
}

.profile-name {
    font-size: 1.75em;
    height: 100%;
    max-height: 7.5em;
    word-spacing: 100vw;
}

.staff-field {
    padding: 0.4em 0;
}

.staff-data {
    padding: 1.8em 0;
}

.button {
    width: fit-content;
	color: white;
    padding: 0.5em 1.8em;
	font-size: 1em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
	background-color: #5076b6;
	border-radius: 0.4em;
	border-style: hidden;
}
</style>
