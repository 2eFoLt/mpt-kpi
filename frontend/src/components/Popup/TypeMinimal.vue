<template>
  <transition name="left">
    <Teleport to="body">
      <aside
        :key="key"
        class="minimal-modal-window minimal-modal-window_centralize"
      >
        <div class="minimal-modal-window__backdrop" @click="$emit('close')" />

        <section class="minimal-modal-window__content">
          <button
            class="minimal-modal-window__close hover-scaling"
            @click="$emit('close')"
          >
            <img src="@/../static/icons/cross.svg" alt="Close" />
          </button>
          <slot />
        </section>
      </aside>
    </Teleport>
  </transition>
</template>

<style lang="sass" scoped>
button {
    background: none;
    border: none;
}
.minimal-modal-window {
	position: fixed;
	left: 0;
	top: 0;
	min-width: 100vw;
	min-height: 100vh;
	z-index: 21;
	transition: all .2s ease;
}

.minimal-modal-window_centralize {
	display: flex;
    align-items: center;
	justify-content: center;
}

.v-enter,
.v-leave-to {
    .minimal-modal-window__backdrop {
		opacity: 0;
    }
    .minimal-modal-window__content {
		opacity: 0;
    }
}

.v-enter-to,
.v-leave {
    .minimal-modal-window__backdrop {
		opacity: 1;
    }
    .minimal-modal-window__content {
		opacity: 1;
    }
}


.minimal-modal-window__backdrop {
    position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	transition: opacity .2s ease;
	background: rgba(0, 0, 0, .67);
}

.minimal-modal-window__content {
	position: relative;
}

.minimal-modal-window__close {
	position: absolute;
	width: 1em;
	top: .7em;
	right: .7em;
	z-index: 1;
}

img {
    width: 100%;
}
</style>
