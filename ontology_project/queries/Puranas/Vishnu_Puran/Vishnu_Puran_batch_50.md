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

### Verse 1 (Vishnu Puran 0.981)
- **Original**: 97 रूपौदार्यगुणोपेतस्तथा चाप्सरसां गण: । क्षीरोदधे: समुत्पन्नो मैत्रेय परमाद्भधुत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.982)
- **Original**: ततः शीतांशुरभवजगूहे त॑ महेश्वर: । जगृहुश्न विष नागा: क्षीरोदाब्यिसमुत्थितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.983)
- **Original**: 97 ततो धन्वन्तरिरदेव: श्रेताम्जरधरस्स्वयम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.984)
- **Original**: बिप्रत्कमण्डलुं पूर्णममृतस्य समुत्यित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.985)
- **Original**: 98 ततः स्वस्थमनस्कास्ते सर्वे दैतेयदानवा: । बभृवुर्मुदिता: सर्वे मैत्रेय मुनिभति: सह
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.986)
- **Original**: 99 तत्ः स्फुरत्कान्तिमती विकासिकमले स्थिता । श्रीदेंगी पयसस्तस्मादुद्धता धृतपड्ुजा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.987)
- **Original**: 1900 तां तुद्ठ॒वुर्मुदा युक्ता: श्रीसूक्तेन महर्षय:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.988)
- **Original**: 109 विश्वावसुमुखास्तस्या गन्धर्वा: पुस्तो जगुः । घृतान्नीप्रमुखास्तत्र ननृतुश्चाप्सरशोगणा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.989)
- **Original**: 102 गड्ढाद्या: सरितस्तोयै: स्त्रानार्थमुपतस्थिरे । दिग्जा हेमपात्रस्थमादाय विमलं जल्म्‌ । स्नापयाञ्जक्रिरे देवीं सर्वस्लेकमहेश्वरीम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.990)
- **Original**: 103 क्षीरोंदों रूपधृक्तस्थे मालामम्लानपड्ुजाम्‌। ददौ विभूषणान्यड्ले विश्वकर्मा चकार ह
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.991)
- **Original**: 104 दिव्यमाल्याम्बरधरा स्राता भूषणभूषिता । पश्यतां सर्वदेवानां ययौ वक्षःस्थलं हरे:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.992)
- **Original**: 1905 प्रथम अंझ 35 खींचने लगे थे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.993)
- **Original**: तथा हें मैत्रेय ! एक अन्य विश्ञाल रूपसे जो देवता और दैत्योंको दिखायी नहीों देता या, श्रीकेशवने कपरसे पर्वतकों दबा रस्ता था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.994)
- **Original**: भगवान्‌ श्रीहरि अपने तेजसे नागराज वासुकिमें बलका सझ्ार करते थे और अपने अन्य तेजसे थे देखताओंका बल बढ़ा रहे थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.995)
- **Original**: इस प्रकार, देखता और दानबोंड्राए क्षीर-समुद्रके सथे जानेपर पहले हवि (यज्ञ-साम्रप्री) की आश्रयरूपा सुरपूजिता कामधेनु उत्पन्न हुई
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.996)
- **Original**: है महामुने । उस स्रमय देव और दानवगण अति आनन्दित हुए और उसकी ओर चित्त खिंच जानेसे उनकी टक्टकी बैंध गयी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.997)
- **Original**: फिर स्वर्गलोकमें 'यह क्या है ? यह क्या है ?' इस प्रकार बिच्ता करते हुए सिद्धोंके समक्ष मदसे घूमते हुए नेत्रॉचाली वारुणीदेवी प्रकट हुई
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.998)
- **Original**: और पुनः मन्थन करनेपर उस क्षीर-सागरसे, अपनी गज्से ब्रिलोकीको सुगन्धित करनेवाल्ा तथा सर-सुन्दर्योंका आनन्दवर्धक कल्पवृक्ष उत्पत्र हुआ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.999)
- **Original**: हे मैत्रेय ! तत्पश्नात्‌ क्षीर-सागरसे रूप और ठदारता आदि गुणोंसे युक्त अत्ति अद्भुत अप्सराएँ, प्रकट हुईं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1000)
- **Original**: फिर चन्द्रमा प्रकट हुआ जिसे महादेबजीने ग्रहण कर लिया इसी प्रकार क्षीर-सागरसे उत्पन्न हुए विषको नागेनि ग्रहण किया
- **Translation**: 

---

