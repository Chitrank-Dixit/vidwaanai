# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Rig Ved 0.6081)
- **Original**: मं0 3 सृ0 29 35 2670. वृषो अग्नि: समिध्यते5श्वो न देववाहन: । त॑ हविष्मन्त ईछते
- **Translation**: 

---

### Verse 2 (Rig Ved 0.6082)
- **Original**: बलशाली अश्व जैसे राजा के वाहन को खींच कर ले जाते हैं, उसी प्रकार अग्निदिव देवताओं तक हवि पहुँचाते हैं । ऐसे अग्निदेव उत्तम प्रकार से प्रदीप्त हुए, यजमान की स्तुतियों को प्राप्त करते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.6083)
- **Original**: 2671. वृषणं त्वा बय॑ वृषन्वृषण: समिधीमहि। अग्ने दीद्यतं बृहत्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.6084)
- **Original**: है बलवान्‌ अग्निदेव ! घृतादि की हवि प्रदान करने वाले हम, शक्तिशाली, तेजस्वी और महान्‌ आपको (अग्नि को) प्रदीप्त करते हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.6085)
- **Original**: [ सूक्त - 28 ] [ऋषि - विश्वापरित्र गाधित । देवता - अग्नि । छन्द - 1- 2, 6 गायत्री; 3 उष्णिक्‌ ; 4 त्रिष्ट॒प; 5 जगती । ] 2672. अग्ने जुषस्व नो हवि: पुरो्ठाशं जातवेद: । प्रात: सावे धियावसो
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6086)
- **Original**: है ज़ातवेदा अग्निदेव ! हमारी स्तुतियाँ आपके पास निवास करती हैं । आप प्रातः सबन में हमारे पास आकर पुरोडाश और हव्यादि का सेवन करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.6087)
- **Original**: 2673. पुरोब्ठा अग्ने पचतस्तुभ्यं वा घा परिष्कृतः
- **Translation**: 

---

### Verse 8 (Rig Ved 0.6088)
- **Original**: तं जुषस्व यविष्ठ्य
- **Translation**: 

---

### Verse 9 (Rig Ved 0.6089)
- **Original**: हे अतिशय युवा अग्निदेव ! आपके लिए पुरोडाश पकाया गया है और उसे घृतादि द्वारा सुसंस्कृत किया गया है, आप उसे ग्रहण करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.6090)
- **Original**: 2674. अग्ने वीहि पुरोछाशमाहुतं तिरो अह्नध्मम्‌। सहसः सूनुरस्यध्वरे हित:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.6091)
- **Original**: है अभ्निदेव ! सख्या वेला में समर्पित किये गये पुरोडाश का आप सेवन करें । आप बल के पुत्र हैं और यज्ञ में सर्वहितकारी हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.6092)
- **Original**: 2675, माध्यन्दिने सबने जातवेदः पुरोक्ाशमिह कवे जुषघस्व
- **Translation**: 

---

### Verse 13 (Rig Ved 0.6093)
- **Original**: अग्ने यहस्य तब भागशेेयं न प्र मिनन्ति विदथेषु धीरा:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.6094)
- **Original**: मेधावी और सर्व भूत ज्ञाता हे अग्निदेव ! इस यज्ञ में माध्यन्दिन सवन के समय समर्पित पुरोडाश का आप सेवन करें । यज्ञ में धीर अध्वर्युगण आपके भाग को नष्ट नहीं करते
- **Translation**: 

---

### Verse 15 (Rig Ved 0.6095)
- **Original**: 2676. अग्ने तृतीये सबने हि कानिषः पुरोछाशं सहसः सूनवाहुतम्‌ । अथा देवेष्वध्वरं विपन्यया धा रलवन्तममृतेषु जागृविम्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.6096)
- **Original**: बल के पुत्र हे अग्निदेव ! तीसरे सन में दिए गए पुरोडाश को आप स्वीकार करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.6097)
- **Original**: तदनन्तर अविनाशी, रलधारक, चैतन्यस्वरूप सोम क्र देवों के पास पहुँचाएँ
- **Translation**: 

---

### Verse 18 (Rig Ved 0.6098)
- **Original**: 2677. अन्ने वृधान आहुतिं पुरोछ्ाशं जातवेद: । जुषस्व तिरोअह्नद्यम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.6099)
- **Original**: हे जातवेदा अभ्निदेव ! विवर्धमान आप दिन के अन्त में समर्पित पुरोडाश रूपी आहुतियों का सेवन करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.6100)
- **Original**: [ सूक्त - 29 ] [ऋषि - विश्वामित्र गाधिन । देवता - अग्कि; 5 अग्नि, अथवा ऋत्विजू । छद - विष्टप 1,4, 10, 12 अनुष्टफ्‌ 6, 11, 14, 15 जगती ] 2678. अस्तीदमधिम्रन्थनमस्ति प्रजनन॑ कृतम्‌। एतां विश्पत्नीमा भराग्निं मन्धाम पूर्वथा
- **Translation**: 

---

