<template>
  <section id="workspace">
    <div class="section-header">
      <h1 class="section-header-title">Сертификаты</h1>
      <div class="add-certificate">
        <svg
          width="75"
          height="75"
          viewBox="0 0 59 58"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M29.4999 54.8422V3.52637M3.84204 29.1843H55.1578"
            stroke="#5076B6"
            stroke-width="6"
            stroke-linecap="round"
          />
        </svg>
      </div>
    </div>
    <div class="certificate-list"></div>
  </section>
</template>

<style lang="sass" scoped>
#workspace {
    color: white;
	display: flex;
    flex-direction: column;
    gap: 3em;

    padding: 1.5em 2.75em;
}

.certificate-list {
    display: flex;
	justify-content: space-between;
    flex-direction: row;
    height: 100%;
    width: 100%;
    max-height: 10em;
}

.add-certificate {
    width: 100%;
    height: 8.6em;

    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #DEF1FF;
    border-radius: 0.75em;
    cursor: pointer;
}

.section-header-title {
    font-size: 2.5em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
    padding-bottom: 0.5em;
}
</style>
