<template>
  <div>
    <component
      :is="currentMenu"
      :right="side === 'right' ? true: false"
    >
      <a @click="onPatientInputView">
        <i class="fa fa-fw fa-newspaper-o"></i>
        <span>送检信息</span>
      </a>
      <a @click="onClickDatasetView">
        <i class="fa fa-fw fa-star-o"></i>
        <span>数据分析</span>
      </a>
      <a @click="onClickUpload">
        <i class="fa fa-fw fa-bell-o"></i>
        <span>流式数据上传</span>
      </a>
      <a @click="onClickGenReport">
        <i class="fa fa-fw fa-envelope-o"></i>
        <span>报表</span>
      </a>
    </component>
    <main
      id="page-wrap"
      style="height=100%"
    >
      <div>
        <component :is="currentView"></component>
      </div>
    </main>
  </div>
</template>

<script>
import slide from './Menu/slide.vue'
import bubble from './Menu/bubble.vue'
import elastic from './Menu/elastic.vue'
import falldown from './Menu/fallDown.vue'
import push from './Menu/push'
import pushrotate from './Menu/pushRotate.vue'
import reveal from './Menu/reveal.vue'
import scaledown from './Menu/scaleDown.vue'
import scalerotate from './Menu/scaleRotate.vue'
import stack from './Menu/stack.vue'
import Menu from './Menu.vue'
import WelcomeView from './WelcomeView.vue'
import DatasetView from './DatasetView.vue'
import UploadView from './UploadView.vue'
import PatientInputView from './PatientInputView.vue'
import ReportGenView from './ReportGenView.vue'
export default {
  name: 'MainView',
  data () {
    return {
      menus: {
        slide: { buttonText: 'Slide' },
        push: { buttonText: 'Push' },
        pushRotate: { buttonText: 'Push Rotate' },
        reveal: { buttonText: 'Reveal' },
        scaleDown: { buttonText: 'Scale Down' },
        scaleRotate: { buttonText: 'Scale Rotate' },
        bubble: { buttonText: 'Bubble' },
        fallDown: { buttonText: 'Fall Down' }
      },
      side: 'left',
      currentMenu: 'push',
      currentView: 'WelcomeView'
    }
  },
  components: {
    slide,
    bubble,
    elastic,
    push,
    pushrotate,
    scaledown,
    scalerotate,
    reveal,
    stack,
    falldown,
    Menu,
    WelcomeView,
    DatasetView,
    UploadView,
    PatientInputView,
    ReportGenView
  },
  methods: {
    onClickDatasetView () {
      this.currentView = 'DatasetView'
    },
    onClickUpload () {
      this.currentView = 'UploadView'
    },
    onPatientInputView () {
      this.currentView = 'PatientInputView'
    },
    onClickGenReport () {
      this.currentView = 'ReportGenView'
    },
    onClickDefault () {
      this.currentView = 'WelcomeView'
    }
  }
}
</script>

<style lang="less">
*,
*:after,
*:before {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  height: 100%;
}
body {
  height: 100%;
  color: #fffce1;
  font-family: 'Raleway', Arial, sans-serif;
  margin: 0px;
}
#app {
  height: 100%;
}
a {
  color: #4e4a46;
  text-decoration: none;
  &:hover,
  &:focus {
    color: #c94e50;
  }
}
main {
  height: 100%;
  padding: 3em 2em;
  text-align: center;
  background: #b4bad2;
  overflow: auto;
}
h1 {
  font-weight: 800;
  font-size: 3.75em;
}
.description {
  max-width: 20em;
  margin: 1.2em auto 1em;
  line-height: 1.3em;
  font-weight: 400;
}
.demo-buttons {
  font-size: 1em;
  max-width: 1200px;
  margin: 2em auto 3em;
  padding: 0 10em;
  a {
    display: inline-block;
    margin: 0.75em;
    padding: 1.35em 1.1em;
    width: 15em;
    background: #fffce1;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 800;
    border-top-left-radius: 20px 50px;
    border-top-right-radius: 20px 50px;
    border-bottom-right-radius: 20px 50px;
    border-bottom-left-radius: 20px 50px;
    cursor: pointer;
    &.currentDemo {
      background: #c94e50;
      color: #fffce1;
    }
  }
}
.sideButton {
  display: inline-block;
  width: 5em;
  height: 2.5em;
  line-height: 2.5em;
  cursor: pointer;
  background: #fffce1;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.8em;
  font-weight: 800;
  &.left {
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
  }
  &.right {
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
  }
  &.active {
    background: #c94e50;
    color: #fffce1;
  }
}
@media screen and (max-width: 40em) {
  main {
    font-size: 80%;
  }
  h1 {
    padding-top: 1em;
    font-size: 2.5em;
  }
  .demo-buttons {
    max-width: 900px;
    padding: 0 2em;
  }
}
//
// Burger menu custom styles
//
.bm-burger-button {
  position: absolute;
  width: 36px;
  height: 30px;
  left: 36px;
  top: 36px;
}
.right .bm-burger-button {
  left: initial;
  right: 36px;
}
.bm-burger-bars {
  background: #373a47;
}
.bm-morph-shape {
  fill: #373a47;
}
.bm-menu {
  background: #373a47;
  a {
    color: #b8b7ad;
    &:hover,
    &:focus {
      color: #c94e50;
    }
  }
}
//
// Mixins
//
.menu-1 {
  .bm-cross {
    background: #bdc3c7;
  }
  .bm-menu {
    padding: 2.5em 1.5em 0;
    font-size: 1.15em;
  }
}
.menu-2 {
  .bm-cross {
    background: #999;
  }
  .bm-menu {
    padding: 3.4em 1em 0;
  }
  a {
    padding: 1em;
  }
  i {
    font-size: 1.7em;
    vertical-align: middle;
    color: #282a35;
  }
}
.menu-3 {
  .bm-cross {
    background: #888;
  }
  .bm-menu {
    padding: 2em 1em;
    font-size: 1.15em;
  }
  i {
    opacity: 0.5;
  }
  span {
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 0.75em;
  }
}
.menu-4 {
  .bm-cross {
    background: #888;
  }
  h2 {
    margin: 0 auto;
    padding: 2em 1em;
    color: rgba(0, 0, 0, 0.4);
    box-shadow: inset 0 -1px rgba(0, 0, 0, 0.2);
    i {
      margin-left: 0.2em;
    }
    span {
      font-size: 1.6em;
      font-weight: 700;
    }
  }
  a {
    padding: 1em;
    text-transform: uppercase;
    transition: background 0.3s, box-shadow 0.3s;
    box-shadow: inset 0 -1px rgba(0, 0, 0, 0.2);
    span {
      letter-spacing: 1px;
      font-weight: 400;
    }
    &:hover,
    &:focus {
      background: rgba(0, 0, 0, 0.2);
      box-shadow: inset 0 -1px rgba(0, 0, 0, 0);
      color: #b8b7ad;
    }
  }
}
</style>
