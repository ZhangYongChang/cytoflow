REPORT_TEMPLATE = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <title>Report</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
  <style type="text/css">
    .pdfTopImg {
      Font: 8pt Arial;
      border: 0px;
      text-align: left;
      vertical-align: top;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .pdfCompanyName {
      color: #17365D;
      Font: bold 14pt 楷体;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .pdfNumber {
      Font: 9pt 微软雅黑;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .pdfReportName {
      background-color: #FFFFFF;
      Font: bold 18pt 宋体;
      border: 0px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sa5f9e952 {
      background-color: #FFFFFF;
      Font: 12pt 宋体;
      border: 0px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sef8386c8 {
      Font: 8pt Arial;
      border: 0px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s7afdc30c {
      Font: 8pt Arial;
      border: 0px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sa6be309e {
      Font: 11pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s071be6ee {
      Font: 11pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .sb60498d5 {
      Font: 11pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .se62e4896 {
      Font: 8pt Arial;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s28049f3b {
      Font: 8pt Arial;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sf4285fb4 {
      background-color: #FFFFFF;
      Font: 10pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s3d6c5dc2 {
      background-color: #FFFFFF;
      Font: 12pt 宋体;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s85a38a3f {
      background-color: #FFFFFF;
      Font: 10pt 宋体;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sd1fcef5c {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s7b0a07d2 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sc8e3ace7 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s989f9cc4 {
      Font: 8pt Arial;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sfe069fd3 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s44b6ac38 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      border-bottom-color: #000000;
      border-bottom-style: solid;
      border-bottom-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s096698bd {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-top-color: #000000;
      border-top-style: solid;
      border-top-width: 1px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .se40b9286 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-left-color: #000000;
      border-left-style: solid;
      border-left-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .s0dd5de56 {
      background-color: #FFFFFF;
      Font: 12pt 宋体;
      border: 0px;
      text-align: left;
      vertical-align: bottom;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .s749bc175 {
      background-color: #FFFFFF;
      Font: 11pt 宋体;
      border: 0px;
      border-right-color: #000000;
      border-right-style: solid;
      border-right-width: 1px;
      text-align: center;
      vertical-align: middle;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .s57d589e1 {
      background-color: #FFFFFF;
      Font: 12pt 宋体;
      border: 0px;
      text-align: left;
      vertical-align: top;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .s27c6134d {
      background-color: #FFFFFF;
      Font: 10pt 宋体;
      border: 0px;
      text-align: left;
      vertical-align: top;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }

    .sd051d7c6 {
      Font: 8pt Arial;
      border: 0px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sbbd8345b {
      Font: 10pt 微软雅黑;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .sdad73b2c {
      Font: 10pt 微软雅黑;
      border: 0px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .scd1ba1ce {
      Font: 10pt 微软雅黑;
      border: 0px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s9080b158 {
      color: #548DD4;
      Font: 10pt 微软雅黑;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .se8c0b7e5 {
      background-color: #FFFFFF;
      Font: 10pt 宋体;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s99e83711 {
      Font: 10pt 宋体;
      border: 0px;
      text-align: right;
      vertical-align: middle;
      line-height: 1.15em;
      white-space: nowrap;
      overflow: hidden;
    }

    .s736247aa {
      Font: bold 11pt 宋体;
      border: 0px;
      text-align: left;
      vertical-align: middle;
      line-height: 1.15em;
      word-wrap: break-word;
      overflow: hidden;
    }
  </style>
</head>

<body style="margin:3;">
  <table cellspacing="0" cellpadding="0" border="0" style="border-width:0px;width:718px;border-collapse:collapse;">
    <tr style="height:21px;">
      <td class="pdfTopImg" colspan="26" style="height:21px;width:416px;line-height:0;">
        <img src="1.Jpeg" style="height:21px;width:416px;border-width:0px;" />
      </td>
      <td class="pdfCompanyName" colspan="21" style="max-height:21px;height:21px;width:302px;max-width:302px;">
        武汉康圣达医学检验所
      </td>
    </tr>
    <tr style="height:2px;">
      <td class="pdfTopImg" colspan="46" style="height:2px;width:711px;line-height:0;">
        <img src="2.Jpeg" style="height:2px;width:711px;border-width:0px;" />
      </td>
      <td style="border:0px;height:2px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td class="pdfTopImg" colspan="27" rowspan="4" style="height:33px;width:438px;line-height:0;">
        <img src="3.Jpeg" style="height:33px;width:438px;border-width:0px;" />
      </td>
      <td class="pdfNumber" colspan="20" rowspan="2" style="max-height:15px;height:15px;width:280px;max-width:280px;">
        武汉高新大道666号光谷生物城D2-1
      </td>
    </tr>
    <tr style="height:8px;">

    </tr>
    <tr style="height:3px;">
      <td class="pdfNumber" colspan="20" rowspan="2" style="max-height:18px;height:18px;width:280px;max-width:280px;">
        400-736-1666 800-810-0579</td>
    </tr>
    <tr style="height:15px;">

    </tr>
    <tr style="height:4px;">
      <td class="pdfTopImg" colspan="46" style="height:4px;width:711px;line-height:0;"><img
          src="4.Jpeg"
          style="height:4px;width:711px;border-width:0px;" /></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:38px;">
      <td class="pdfReportName" colspan="47" style="max-height:38px;height:38px;width:718px;max-width:718px;">
        血液肿瘤免疫分型报告单
      </td>
    </tr>
    <tr style="height:22px;">
      <td class="sa5f9e952" colspan="47" style="max-height:22px;height:22px;width:718px;max-width:718px;">
      Hematological Tumor Immunotype Report</td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:15px;"></td>
      <td class="sef8386c8" style="height:8px;width:4px;"></td>
      <td class="sef8386c8" style="height:8px;width:19px;"></td>
      <td class="sef8386c8" style="height:8px;width:15px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:30px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:16px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:23px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:38px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:15px;"></td>
      <td class="sef8386c8" style="height:8px;width:15px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:37px;"></td>
      <td class="sef8386c8" style="height:8px;width:23px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:22px;"></td>
      <td class="sef8386c8" style="height:8px;width:38px;"></td>
      <td class="sef8386c8" style="height:8px;width:23px;"></td>
      <td class="sef8386c8" style="height:8px;width:22px;"></td>
      <td class="sef8386c8" style="height:8px;width:38px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:23px;"></td>
      <td class="sef8386c8" style="height:8px;width:22px;"></td>
      <td class="sef8386c8" style="height:8px;width:23px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:15px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:30px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:8px;"></td>
      <td class="sef8386c8" style="height:8px;width:34px;"></td>
      <td class="sef8386c8" style="height:8px;width:7px;"></td>
      <td class="sef8386c8" style="height:8px;width:4px;"></td>
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:32px;">
      <td style="border:0px;height:32px;width:8px;"></td>
      <td class="s7afdc30c" style="height:32px;width:7px;"></td>
      <td class="sa6be309e" colspan="6" style="max-height:31px;height:31px;width:90px;max-width:90px;">
        &nbsp;姓名(Name)：
      </td>
      <td class="s071be6ee" colspan="8" style="height:31px;width:112px;">
        {{specimen.name}}
      </td>
      <td class="sa6be309e" colspan="5" style="max-height:31px;height:31px;width:82px;max-width:82px;">
        &nbsp;性别(Sex)：
      </td>
      <td class="sb60498d5" colspan="3" style="height:31px;width:52px;">
        {{specimen.sex}}
      </td>
      <td class="sa6be309e" colspan="3" style="max-height:31px;height:31px;width:82px;max-width:82px;">
        &nbsp;年龄(Age)：
      </td>
      <td class="sb60498d5" colspan="4" style="height:31px;width:60px;">
        {{specimen.age}}岁
      </td>
      <td class="sa6be309e" colspan="7" style="max-height:31px;height:31px;width:105px;max-width:105px;">
        &nbsp;标本编号(No.)：
      </td>
      <td class="sb60498d5" colspan="7" style="max-height:31px;height:31px;width:97px;max-width:97px;">
        {{specimen.specimenno}}
      </td>
      <td class="se62e4896" style="height:32px;width:8px;"></td>
      <td style="border:0px;height:32px;width:7px;"></td>
    </tr>
    <tr style="height:30px;">
      <td style="border:0px;height:30px;width:8px;"></td>
      <td class="s7afdc30c" style="height:30px;width:7px;"></td>
      <td class="sa6be309e" colspan="10" rowspan="2" style="max-height:31px;height:31px;width:143px;max-width:143px;">
        &nbsp;送检医院(Hospital)：
      </td>
      <td class="s071be6ee" colspan="12" rowspan="2" style="max-height:31px;height:31px;width:195px;max-width:195px;">
        {{specimen.hospital}}
      </td>
      <td class="sa6be309e" colspan="6" rowspan="2" style="max-height:31px;height:31px;width:135px;max-width:135px;">
        &nbsp;科室(Department)：
      </td>
      <td class="s071be6ee" colspan="15" rowspan="2" style="height:31px;width:211px;">
        {{specimen.department}}
      </td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td style="border:0px;height:30px;width:7px;"></td>
    </tr>
    <tr style="height:2px;">
      <td style="border:0px;height:2px;width:8px;"></td>
      <td class="s7afdc30c" style="height:2px;width:7px;"></td>
      <td class="se62e4896" style="height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
    </tr>
    <tr style="height:30px;">
      <td style="border:0px;height:30px;width:8px;"></td>
      <td class="s7afdc30c" style="height:30px;width:7px;"></td>
      <td class="sa6be309e" colspan="8" style="max-height:29px;height:29px;width:113px;max-width:113px;">
        &nbsp;床号(Bed No.)：
      </td>
      <td class="sb60498d5" colspan="14" style="height:29px;width:225px;">
        {{specimen.bedno}}
      </td>
      <td class="sa6be309e" colspan="4" style="max-height:29px;height:29px;width:120px;max-width:120px;">
        &nbsp;送检医生(Dr.)：
      </td>
      <td class="sb60498d5" colspan="17" style="height:29px;width:226px;">
        {{specimen.doctor}}
      </td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td style="border:0px;height:30px;width:7px;"></td>
    </tr>
    <tr style="height:2px;">
      <td style="border:0px;height:2px;width:8px;"></td>
      <td class="s7afdc30c" style="height:2px;width:7px;"></td>
      <td class="sa6be309e" colspan="11" rowspan="2" style="max-height:24px;height:24px;width:150px;max-width:150px;">
        &nbsp;标本类型(Specimen)：
      </td>
      <td class="sb60498d5" colspan="11" rowspan="2" style="height:24px;width:188px;">
        {{specimen.specimentype}}
      </td>
      <td class="sa6be309e" colspan="10" rowspan="2" style="max-height:24px;height:24px;width:211px;max-width:211px;">
        &nbsp;病历号(Medical Record No.)：
      </td>
      <td class="s071be6ee" colspan="11" rowspan="2" style="max-height:24px;height:24px;width:135px;max-width:135px;">
        {{specimen.caseno}}
      </td>
      <td class="se62e4896" style="height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
    </tr>
    <tr style="height:23px;">
      <td style="border:0px;height:23px;width:8px;"></td>
      <td class="s7afdc30c" style="height:23px;width:7px;"></td>
      <td class="se62e4896" style="height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
    </tr>
    <tr style="height:24px;">
      <td style="border:0px;height:24px;width:8px;"></td>
      <td class="s7afdc30c" style="height:24px;width:7px;"></td>
      <td class="sa6be309e" colspan="17" style="max-height:23px;height:23px;width:241px;max-width:241px;">
        &nbsp;采集时间(Specimen Sampling Time)：
      </td>
      <td class="sb60498d5" colspan="5" style="max-height:23px;height:23px;width:97px;max-width:97px;">
        {{specimen.collecttime}}
      </td>
      <td class="sa6be309e" colspan="13" style="max-height:23px;height:23px;width:241px;max-width:241px;">
        &nbsp;接收时间(Specimen Receive Time)：
      </td>
      <td class="sb60498d5" colspan="8" style="max-height:23px;height:23px;width:105px;max-width:105px;">
        {{specimen.recvtime}}
      </td>
      <td class="se62e4896" style="height:24px;width:8px;"></td>
      <td style="border:0px;height:24px;width:7px;"></td>
    </tr>
    <tr style="height:23px;">
      <td style="border:0px;height:23px;width:8px;"></td>
      <td class="s7afdc30c" style="height:23px;width:7px;"></td>
      <td class="sa6be309e" colspan="12" style="max-height:22px;height:22px;width:158px;max-width:158px;">
        &nbsp;临床诊断(Diagnosis)：
      </td>
      <td class="sb60498d5" colspan="31" style="height:22px;width:528px;"></td>
      <td class="se62e4896" style="height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:4px;"></td>
      <td class="s28049f3b" style="height:7px;width:19px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:30px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:16px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:37px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:30px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:34px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:4px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td class="s7afdc30c" style="height:8px;width:7px;"></td>
      <td class="sf4285fb4" colspan="43" style="height:7px;width:687px;"></td>
      <td class="se62e4896" style="height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:22px;">
      <td style="border:0px;height:22px;width:8px;"></td>
      <td class="s7afdc30c" style="height:22px;width:7px;"></td>
      <td class="s3d6c5dc2" colspan="43"
        style="max-height:22px;height:22px;white-space:pre-wrap;max-width:688px;width:688px;"> 获取和分析细胞数(Total Events)：20000 CD45/SSC 设门 (CD45/SSC Gates)</td>
      <td class="se62e4896" style="height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
    </tr>
    <tr style="height:23px;">
      <td style="border:0px;height:23px;width:8px;"></td>
      <td class="s7afdc30c" style="height:23px;width:7px;"></td>
      <td class="s3d6c5dc2" colspan="43"
        style="max-height:23px;height:23px;white-space:pre-wrap;max-width:688px;width:688px;"> 各群细胞占有核细胞比例(Cell Population Proportion)：</td>
      <td class="se62e4896" style="height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td class="s7afdc30c" style="height:7px;width:7px;"></td>
      <td class="s85a38a3f" colspan="43" style="height:7px;width:688px;"></td>
      <td class="se62e4896" style="height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:30px;">
      <td style="border:0px;height:30px;width:8px;"></td>
      <td class="s7afdc30c" style="height:30px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="4" style="height:30px;width:53px;"></td>
      <td class="s7afdc30c" style="height:30px;width:8px;"></td>
      <td class="s7b0a07d2" colspan="26" style="max-height:29px;height:29px;width:467px;max-width:467px;">
        淋巴细胞(绿色)Lymphocytes(Green)</td>
      <td class="s7b0a07d2" colspan="6" style="height:29px;width:90px;">
        {{specimen.green}}
      </td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="5" style="height:30px;width:60px;"></td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td style="border:0px;height:30px;width:7px;"></td>
    </tr>
    <tr style="height:31px;">
      <td style="border:0px;height:31px;width:8px;"></td>
      <td class="s7afdc30c" style="height:31px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="4" style="height:31px;width:53px;"></td>
      <td class="s7afdc30c" style="height:31px;width:8px;"></td>
      <td class="s7b0a07d2" colspan="26" style="max-height:30px;height:30px;width:467px;max-width:467px;">
        前体B淋巴细胞(黄色)Precursor B Lymphocytes(Yellow)</td>
      <td class="s7b0a07d2" colspan="6" style="height:30px;width:90px;">
        {{specimen.yellow}}
      </td>
      <td class="se62e4896" style="height:31px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="5" style="height:31px;width:60px;"></td>
      <td class="se62e4896" style="height:31px;width:8px;"></td>
      <td style="border:0px;height:31px;width:7px;"></td>
    </tr>
    <tr style="height:30px;">
      <td style="border:0px;height:30px;width:8px;"></td>
      <td class="s7afdc30c" style="height:30px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="4" style="height:30px;width:53px;"></td>
      <td class="s7afdc30c" style="height:30px;width:8px;"></td>
      <td class="s7b0a07d2" colspan="26" style="max-height:29px;height:29px;width:467px;max-width:467px;">
        异常细胞群(红色)Abnormal cells(Red)</td>
      <td class="s7b0a07d2" colspan="6" style="height:29px;width:90px;">
        {{specimen.red}}
      </td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="5" style="height:30px;width:60px;"></td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td style="border:0px;height:30px;width:7px;"></td>
    </tr>
    <tr style="height:30px;">
      <td style="border:0px;height:30px;width:8px;"></td>
      <td class="s7afdc30c" style="height:30px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="4" style="height:30px;width:53px;"></td>
      <td class="s7afdc30c" style="height:30px;width:8px;"></td>
      <td class="s7b0a07d2" colspan="26" style="max-height:29px;height:29px;width:467px;max-width:467px;">
        有核红区域细胞(紫色)Nucleated erythrocytes region(Purple)</td>
      <td class="s7b0a07d2" colspan="6" style="height:29px;width:90px;">
        {{specimen.purple}}
      </td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="5" style="height:30px;width:60px;"></td>
      <td class="se62e4896" style="height:30px;width:8px;"></td>
      <td style="border:0px;height:30px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="4" rowspan="2" style="height:7px;width:53px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:30px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:16px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:23px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:38px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:15px;"></td>
      <td class="s989f9cc4" style="height:4px;width:15px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:37px;"></td>
      <td class="s989f9cc4" style="height:4px;width:23px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:22px;"></td>
      <td class="s989f9cc4" style="height:4px;width:38px;"></td>
      <td class="s989f9cc4" style="height:4px;width:23px;"></td>
      <td class="s989f9cc4" style="height:4px;width:22px;"></td>
      <td class="s989f9cc4" style="height:4px;width:38px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:23px;"></td>
      <td class="s989f9cc4" style="height:4px;width:22px;"></td>
      <td class="s989f9cc4" style="height:4px;width:23px;"></td>
      <td class="s989f9cc4" style="height:4px;width:7px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:15px;"></td>
      <td class="s989f9cc4" style="height:4px;width:8px;"></td>
      <td class="s989f9cc4" style="height:4px;width:30px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="5" rowspan="2" style="height:7px;width:60px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:3px;">
      <td style="border:0px;height:3px;width:8px;"></td>
      <td class="s7afdc30c" style="height:3px;width:7px;"></td>
      <td class="sfe069fd3" colspan="34" style="height:3px;width:575px;"></td>
      <td class="se62e4896" style="height:3px;width:8px;"></td>
      <td style="border:0px;height:3px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="s44b6ac38" colspan="43" style="height:4px;width:688px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:4px;"></td>
      <td class="s28049f3b" style="height:8px;width:19px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:30px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:16px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:37px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:30px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:34px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:4px;"></td>
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td class="s7afdc30c" style="height:7px;width:7px;"></td>
      <td class="s096698bd" colspan="43" style="height:6px;width:687px;"></td>
      <td class="se62e4896" style="height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:108px;">
      <td style="border:0px;height:108px;width:8px;"></td>
      <td class="s7afdc30c" style="height:108px;width:7px;"></td>
      <td class="se40b9286" colspan="2" style="max-height:108px;height:108px;width:19px;max-width:19px;">
        <p style="margin:0px;text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;</p>
      </td>
      <td class="s0dd5de56" colspan="40" style="max-height:108px;height:108px;width:665px;max-width:665px;">
        <br>印象：在CD45/SSC点图上设门分析，原始向髓系延伸的分布区域可见异常细胞群体，约占有核细胞的{{specimen.red}}，主要表达HLA-DR、CD4、CD15、CD33、CD38、CD56、CD58、CD123。<br><br><br>提示：异常髓系增殖，AML可能。请结合临床及其他相关检查结果综合判断。<br>
      </td>
      <td class="s749bc175" style="height:108px;width:4px;"></td>
      <td class="se62e4896" style="height:108px;width:8px;"></td>
      <td style="border:0px;height:108px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="9" rowspan="2" style="height:7px;width:121px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:15px;"></td>
      <td style="border:0px;height:4px;width:15px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:37px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="9" rowspan="2" style="height:7px;width:121px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:3px;">
      <td style="border:0px;height:3px;width:8px;"></td>
      <td class="s7afdc30c" style="height:3px;width:7px;"></td>
      <td class="sfe069fd3" colspan="25" style="height:3px;width:446px;"></td>
      <td class="se62e4896" style="height:3px;width:8px;"></td>
      <td style="border:0px;height:3px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="s44b6ac38" colspan="43" style="height:4px;width:688px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:4px;"></td>
      <td class="s28049f3b" style="height:8px;width:19px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:30px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:16px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:37px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:38px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:22px;"></td>
      <td class="s28049f3b" style="height:8px;width:23px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:15px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:30px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:8px;"></td>
      <td class="s28049f3b" style="height:8px;width:34px;"></td>
      <td class="s28049f3b" style="height:8px;width:7px;"></td>
      <td class="s28049f3b" style="height:8px;width:4px;"></td>
      <td style="border:0px;height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td class="s7afdc30c" style="height:7px;width:7px;"></td>
      <td class="s096698bd" colspan="43" style="height:6px;width:687px;"></td>
      <td class="se62e4896" style="height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:55px;">
      <td style="border:0px;height:55px;width:8px;"></td>
      <td class="s7afdc30c" style="height:55px;width:7px;"></td>
      <td class="se40b9286" colspan="2" style="max-height:55px;height:55px;width:19px;max-width:19px;">
        <p style="margin:0px;text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;</p>
      </td>
      <td class="s57d589e1" colspan="40" style="max-height:55px;height:55px;width:665px;max-width:665px;">
        所检测的抗原(Antigens examined in this
        test)：HLA-DR、CD2、CD3、CD4、CD5、CD7、CD8、CD10、CD11b、CD13、CD14、CD15、CD16、CD19、CD20、CD22、CD33、CD34、CD38、CD56、CD58、CD64、CD71、CD117、CD123、MPO、cCD79a、cCD3、TdT、CD45。<br>
      </td>
      <td class="s749bc175" style="height:55px;width:4px;"></td>
      <td class="se62e4896" style="height:55px;width:8px;"></td>
      <td style="border:0px;height:55px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="sd1fcef5c" colspan="9" rowspan="2" style="height:8px;width:121px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:15px;"></td>
      <td style="border:0px;height:4px;width:15px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:37px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:38px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:22px;"></td>
      <td style="border:0px;height:4px;width:23px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="sc8e3ace7" colspan="9" rowspan="2" style="height:8px;width:121px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="sfe069fd3" colspan="25" style="height:4px;width:446px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:4px;">
      <td style="border:0px;height:4px;width:8px;"></td>
      <td class="s7afdc30c" style="height:4px;width:7px;"></td>
      <td class="s44b6ac38" colspan="43" style="height:4px;width:688px;"></td>
      <td class="se62e4896" style="height:4px;width:8px;"></td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:4px;"></td>
      <td class="s28049f3b" style="height:7px;width:19px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:30px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:16px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:37px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:38px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:22px;"></td>
      <td class="s28049f3b" style="height:7px;width:23px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:15px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:30px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:8px;"></td>
      <td class="s28049f3b" style="height:7px;width:34px;"></td>
      <td class="s28049f3b" style="height:7px;width:7px;"></td>
      <td class="s28049f3b" style="height:7px;width:4px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td class="s7afdc30c" style="height:8px;width:7px;"></td>
      <td class="s096698bd" colspan="43" style="height:7px;width:687px;"></td>
      <td class="se62e4896" style="height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:46px;">
      <td style="border:0px;height:46px;width:8px;"></td>
      <td class="s7afdc30c" style="height:46px;width:7px;"></td>
      <td class="se40b9286" colspan="2" style="max-height:46px;height:46px;width:19px;max-width:19px;">
        <p style="margin:0px;text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;</p>
      </td>
      <td class="s27c6134d" colspan="39" style="max-height:46px;height:46px;width:658px;max-width:658px;">
        注：本次检测结果仅对本次标本负责，结果仅供临床医生参考。请结合临床表现、细胞学和遗传学结果进一步确诊。由于标本保存有一定期限，若对报告结果有疑问，请于报告日期起的三天内提出复检申请，逾期不再受理复检。<br>Note:
        The test results are only in charge of the specimen and for clinicians’ reference only.</td>
      <td class="s749bc175" colspan="2" style="height:46px;width:11px;"></td>
      <td class="se62e4896" style="height:46px;width:8px;"></td>
      <td style="border:0px;height:46px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td style="border:0px;height:8px;width:8px;"></td>
      <td class="s7afdc30c" style="height:8px;width:7px;"></td>
      <td class="s44b6ac38" colspan="43" style="height:8px;width:688px;"></td>
      <td class="se62e4896" style="height:8px;width:8px;"></td>
      <td style="border:0px;height:8px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:15px;"></td>
      <td class="s989f9cc4" style="height:7px;width:4px;"></td>
      <td class="s989f9cc4" style="height:7px;width:19px;"></td>
      <td class="s989f9cc4" style="height:7px;width:15px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:30px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:16px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:23px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:38px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:15px;"></td>
      <td class="s989f9cc4" style="height:7px;width:15px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:37px;"></td>
      <td class="s989f9cc4" style="height:7px;width:23px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:22px;"></td>
      <td class="s989f9cc4" style="height:7px;width:38px;"></td>
      <td class="s989f9cc4" style="height:7px;width:23px;"></td>
      <td class="s989f9cc4" style="height:7px;width:22px;"></td>
      <td class="s989f9cc4" style="height:7px;width:38px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:23px;"></td>
      <td class="s989f9cc4" style="height:7px;width:22px;"></td>
      <td class="s989f9cc4" style="height:7px;width:23px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:15px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:30px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:8px;"></td>
      <td class="s989f9cc4" style="height:7px;width:34px;"></td>
      <td class="s989f9cc4" style="height:7px;width:7px;"></td>
      <td class="s989f9cc4" style="height:7px;width:4px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:23px;">
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:4px;"></td>
      <td style="border:0px;height:23px;width:19px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:30px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:16px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:23px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:38px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:37px;"></td>
      <td style="border:0px;height:23px;width:23px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:22px;"></td>
      <td style="border:0px;height:23px;width:38px;"></td>
      <td class="sd051d7c6" colspan="7" rowspan="3" style="height:53px;width:129px;line-height:0;">
        <!--<img src="5.Jpeg" style="height:53px;width:129px;border-width:0px;" />-->
      </td>
      <td style="border:0px;height:23px;width:22px;"></td>
      <td style="border:0px;height:23px;width:23px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:30px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:34px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:4px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
    </tr>
    <tr style="height:7px;">
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td style="border:0px;height:7px;width:15px;"></td>
      <td style="border:0px;height:7px;width:4px;"></td>
      <td style="border:0px;height:7px;width:19px;"></td>
      <td style="border:0px;height:7px;width:15px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:30px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td class="pdfTopImg" colspan="6" rowspan="2" style="height:30px;width:99px;line-height:0;">
        <!--<img src="6.Jpeg" style="height:30px;width:99px;border-width:0px;" />-->
      </td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td style="border:0px;height:7px;width:15px;"></td>
      <td style="border:0px;height:7px;width:15px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:37px;"></td>
      <td style="border:0px;height:7px;width:23px;"></td>
      <td class="sd051d7c6" colspan="3" rowspan="2" style="height:30px;width:68px;"></td>
      <td style="border:0px;height:7px;width:22px;"></td>
      <td style="border:0px;height:7px;width:23px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:15px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:30px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:34px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
      <td style="border:0px;height:7px;width:4px;"></td>
      <td style="border:0px;height:7px;width:8px;"></td>
      <td style="border:0px;height:7px;width:7px;"></td>
    </tr>
    <tr style="height:23px;">
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td class="sbbd8345b" colspan="6" style="max-height:23px;height:23px;width:83px;max-width:83px;">检验者：</td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td class="sdad73b2c" colspan="2" style="max-height:23px;height:23px;width:60px;max-width:60px;">审核者：</td>
      <td class="sdad73b2c" colspan="3" style="max-height:23px;height:23px;width:52px;max-width:52px;">报告日期：</td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:15px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:30px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:34px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
      <td style="border:0px;height:23px;width:4px;"></td>
      <td style="border:0px;height:23px;width:8px;"></td>
      <td style="border:0px;height:23px;width:7px;"></td>
    </tr>
    <tr style="height:22px;">
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:15px;"></td>
      <td style="border:0px;height:22px;width:4px;"></td>
      <td style="border:0px;height:22px;width:19px;"></td>
      <td class="scd1ba1ce" colspan="5" style="max-height:22px;height:22px;width:76px;max-width:76px;">(Analyzer)</td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:23px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:38px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:15px;"></td>
      <td style="border:0px;height:22px;width:15px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td class="scd1ba1ce" colspan="3" style="max-height:22px;height:22px;width:68px;max-width:68px;">(Reviewer)</td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:22px;"></td>
      <td style="border:0px;height:22px;width:38px;"></td>
      <td class="sd051d7c6" colspan="5" style="height:22px;width:98px;line-height:0;">
        <!--<img src="7.Jpeg" style="height:22px;width:98px;border-width:0px;" />-->
      </td>
      <td class="scd1ba1ce" colspan="6" style="max-height:22px;height:22px;width:91px;max-width:91px;">(ReportTime)</td>
      <td style="border:0px;height:22px;width:15px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:30px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:34px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:4px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
    </tr>
    <tr style="height:119px;">
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:15px;"></td>
      <td style="border:0px;height:119px;width:4px;"></td>
      <td style="border:0px;height:119px;width:19px;"></td>
      <td style="border:0px;height:119px;width:15px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:30px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:16px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:23px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:38px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:15px;"></td>
      <td style="border:0px;height:119px;width:15px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:37px;"></td>
      <td style="border:0px;height:119px;width:23px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:22px;"></td>
      <td style="border:0px;height:119px;width:38px;"></td>
      <td style="border:0px;height:119px;width:23px;"></td>
      <td style="border:0px;height:119px;width:22px;"></td>
      <td style="border:0px;height:119px;width:38px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:23px;"></td>
      <td style="border:0px;height:119px;width:22px;"></td>
      <td style="border:0px;height:119px;width:23px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:15px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:30px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:34px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
      <td style="border:0px;height:119px;width:4px;"></td>
      <td style="border:0px;height:119px;width:8px;"></td>
      <td style="border:0px;height:119px;width:7px;"></td>
    </tr>
    <tr style="height:46px;">
      <td style="border:0px;height:46px;width:8px;"></td>
      <td class="sd051d7c6" colspan="16" style="height:46px;width:226px;line-height:0;">
        <img src="8.Jpeg" style="height:46px;width:226px;border-width:0px;" />
      </td>
      <td style="border:0px;height:46px;width:15px;"></td>
      <td class="s9080b158" colspan="27" style="max-height:46px;height:46px;width:454px;max-width:454px;">
        本检测项目及相关技术由美国梅奥医学中心（Mayo Clinic）提供，<br>由康圣环球(Kindstar Global)所属实验室完成中国地区内的验证和使用</td>
      <td style="border:0px;height:46px;width:8px;"></td>
      <td style="border:0px;height:46px;width:7px;"></td>
    </tr>
    <tr style="height:2px;">
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:4px;"></td>
      <td style="border:0px;height:2px;width:19px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:30px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:16px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:37px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:30px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:34px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:4px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
    </tr>
    <tr style="height:1px;">
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:19px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:16px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:37px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td class="se8c0b7e5" colspan="12" rowspan="2" style="height:15px;width:166px;">0</td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:34px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
    </tr>
    <tr style="height:14px;">
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:4px;"></td>
      <td style="border:0px;height:14px;width:19px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:30px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:16px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:37px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:22px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:22px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td class="s99e83711" colspan="5" rowspan="2" style="height:15px;width:60px;">1/3</td>
    </tr>
    {% for img in imgs %}
    <tr style="height:1px;">
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:19px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:16px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:37px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
    </tr>
    <tr style="height:21px;">
      <td class="pdfTopImg" colspan="26" style="height:21px;width:416px;line-height:0;">
        <img src="1.Jpeg" style="height:21px;width:416px;border-width:0px;" /></td>
      <td class="pdfCompanyName" colspan="21" style="max-height:21px;height:21px;width:302px;max-width:302px;">
        武汉康圣达医学检验所
      </td>
    </tr>
    <tr style="height:1px;">
      <td class="pdfTopImg" colspan="46" style="height:1px;width:711px;line-height:0;">
        <img src="9.Jpeg" style="height:1px;width:711px;border-width:0px;" />
      </td>
      <td style="border:0px;height:1px;width:7px;"></td>
    </tr>
    <tr style="height:8px;">
      <td class="pdfTopImg" colspan="27" rowspan="4" style="height:34px;width:438px;line-height:0;">
        <img src="10.Jpeg" style="height:34px;width:438px;border-width:0px;" />
      </td>
      <td class="pdfNumber" colspan="20" rowspan="2" style="max-height:15px;height:15px;width:280px;max-width:280px;">
        武汉高新大道666号光谷生物城D2-1
      </td>
    </tr>
    <tr style="height:7px;"></tr>
    <tr style="height:4px;">
      <td class="pdfNumber" colspan="20" rowspan="2" style="max-height:19px;height:19px;width:280px;max-width:280px;">
        400-736-1666 800-810-0579
      </td>
    </tr>
    <tr style="height:15px;"></tr>
    <tr style="height:4px;">
      <td class="pdfTopImg" colspan="46" style="height:4px;width:711px;line-height:0;">
        <img src="4.Jpeg" style="height:4px;width:711px;border-width:0px;" />
      </td>
      <td style="border:0px;height:4px;width:7px;"></td>
    </tr>
    <tr style="height:22px;">
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td class="s736247aa" editable="12;Text" colspan="40"
        style="max-height:22px;height:22px;width:643px;max-width:643px;">FCM细胞分布：</td>
      <td style="border:0px;height:22px;width:34px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
      <td style="border:0px;height:22px;width:4px;"></td>
      <td style="border:0px;height:22px;width:8px;"></td>
      <td style="border:0px;height:22px;width:7px;"></td>
    </tr>
    <tr style="height:900px;">
      <td class="pdfTopImg" colspan="47" style="height:900px;width:718px;line-height:0;">
        <img src="data:image/png;base64,{{img}}"/>
        <!--<img src="scatter1.Jpeg" style="height:900px;width:718px;border-width:0px;" />-->
      </td>
    </tr>
    <tr style="height:50px;">
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:15px;"></td>
      <td style="border:0px;height:50px;width:4px;"></td>
      <td style="border:0px;height:50px;width:19px;"></td>
      <td style="border:0px;height:50px;width:15px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:30px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:16px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:23px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:38px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:15px;"></td>
      <td style="border:0px;height:50px;width:15px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:37px;"></td>
      <td style="border:0px;height:50px;width:23px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:22px;"></td>
      <td style="border:0px;height:50px;width:38px;"></td>
      <td style="border:0px;height:50px;width:23px;"></td>
      <td style="border:0px;height:50px;width:22px;"></td>
      <td style="border:0px;height:50px;width:38px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:23px;"></td>
      <td style="border:0px;height:50px;width:22px;"></td>
      <td style="border:0px;height:50px;width:23px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:15px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:30px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:34px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
      <td style="border:0px;height:50px;width:4px;"></td>
      <td style="border:0px;height:50px;width:8px;"></td>
      <td style="border:0px;height:50px;width:7px;"></td>
    </tr>
    <tr style="height:45px;">
      <td style="border:0px;height:45px;width:8px;"></td>
      <td class="sd051d7c6" colspan="16" style="height:45px;width:226px;line-height:0;"><img
          src="8.Jpeg"
          style="height:45px;width:226px;border-width:0px;" /></td>
      <td style="border:0px;height:45px;width:15px;"></td>
      <td class="s9080b158" colspan="27" style="max-height:45px;height:45px;width:454px;max-width:454px;">
        本检测项目及相关技术由美国梅奥医学中心（Mayo Clinic）提供，<br>由康圣环球(Kindstar Global)所属实验室完成中国地区内的验证和使用</td>
      <td style="border:0px;height:45px;width:8px;"></td>
      <td style="border:0px;height:45px;width:7px;"></td>
    </tr>
    <tr style="height:2px;">
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:4px;"></td>
      <td style="border:0px;height:2px;width:19px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:30px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:16px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:37px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:38px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:22px;"></td>
      <td style="border:0px;height:2px;width:23px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:15px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:30px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:34px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
      <td style="border:0px;height:2px;width:4px;"></td>
      <td style="border:0px;height:2px;width:8px;"></td>
      <td style="border:0px;height:2px;width:7px;"></td>
    </tr>
    <tr style="height:1px;">
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:19px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:16px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:37px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td class="se8c0b7e5" colspan="12" rowspan="2" style="height:15px;width:166px;">0</td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:34px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
    </tr>
    <tr style="height:14px;">
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:4px;"></td>
      <td style="border:0px;height:14px;width:19px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:30px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:16px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:7px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:15px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:37px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:22px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:23px;"></td>
      <td style="border:0px;height:14px;width:22px;"></td>
      <td style="border:0px;height:14px;width:38px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td style="border:0px;height:14px;width:8px;"></td>
      <td class="s99e83711" colspan="5" rowspan="2" style="height:15px;width:60px;">2/3</td>
    </tr>
    <tr style="height:1px;">
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:4px;"></td>
      <td style="border:0px;height:1px;width:19px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:16px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:37px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:38px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:22px;"></td>
      <td style="border:0px;height:1px;width:23px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:15px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:30px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
      <td style="border:0px;height:1px;width:7px;"></td>
      <td style="border:0px;height:1px;width:8px;"></td>
    </tr>
    {% endfor%}
  </table>
</body>
</html>'''