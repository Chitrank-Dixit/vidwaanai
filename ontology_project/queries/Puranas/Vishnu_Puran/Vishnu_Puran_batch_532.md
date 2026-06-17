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

### Verse 1 (Vishnu Puran 0.10621)
- **Original**: 4 श्रीपराहरजी बोले--हे द्विज ! एक बार महर्षि गास्येसे उनके सालेने यादवोंकी गोष्ठीमें नपुंसक कह दिया। उस समय समस्त यदुबंशो हैँस पड़े
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10622)
- **Original**: तब गार्ग्यने अत्यन्त कुपित हो दक्षिण-समुद्रके तटपर जा यादबसेताको भयभीत करनेवाले पुत्रकों प्राप्तेके लिये तपस्या की
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10623)
- **Original**: उन्होने श्रीमहादेवजीकी उपासना करते हुए केबल लोहचूर्ण भक्षण क्रिया तब भगवान्‌ इकरने बारहवें वर्षमें प्रसन्न होकर उन्हें अभीए वर दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10624)
- **Original**: एक पुत्रहोन यबनराजने महर्षि गार्ग्यकी अत्यन्त सेवाकर उज्हें सत्तुष्ट क्रिया, उसकी खीके सेगसे ही इनके एक भौरेके समान कृष्णवर्ण बाऊक हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10625)
- **Original**: इ7ढ [ अ* 23 त॑ कालयवन नाम राज्ये स्वे यवनेश्वरः । अभिषिच्य बन॑ यातो बज्ाग्रकठिनोरसम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10626)
- **Original**: जिसका वक्षःस्थऊ वज़्के समान कठोर था, अपने राज्यपटपर अभिषिक्त कर स्वयं लनको चला गया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10627)
- **Original**: जलह यवनराज उस कालयवन नामक बालकको, स तु वीर्यमदोन्‍्मत्त: पृथिव्यां बलिनो नृपान्‌ । तदनन्तर वीर्यमदोत्मत्त कालयबनने नास्दजीसे पूछ कि अपृक्छन्नारदस्तस्मे कथयामास यादवान्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10628)
- **Original**: पृथिवीपर बलबान्‌ राजा कौन कौतसे हैं 7 इसपर नारदजीने उसे याटवॉक् ही सबसे अधिक बलशाली बतलाया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10629)
- **Original**: गजाश्ररथसम्पन्नैश्षकार परमोह्ममम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10630)
- **Original**: सहित सहसनों करोड़ म्लेच्छ-सेनाको साथ ले बड़ी भारी 'इव्यवल्छित्न छित्रयानो तैयारी की
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10631)
- **Original**: और यादवोंके भ्रति क्ुदध होकर प्रययो सो. मैत्रेय दिने दिने । प्रतिदिंण [ हाथी, घोड़े आदिके थक जानेपर ) डन यादवाग्रति सामर्षो मथुरां पुरीमु
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10632)
- **Original**: 8 वाहनोंका त्याग करता हुआ [ अन्य वाहनॉपर चढ़कर ] कृष्णोउपि चिन्तयामास क्षपित यादव बलम्‌ । अविच्छित्न-गतिसे मधुरापुरीपर चक्र आया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10633)
- **Original**: कालयननकी चढ़ाई देखकर ] श्रीकृष्णचद्धने सोचा--- म्रागधस्य बल क्षीणं स कालयवनो बली । "यबनोंके साथ युद्ध करनेसे श्तीण हुई यादव-सेना अवश्य हन्तैतदेवमायात॑ यदूनां व्यसन द्विधा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10634)
- **Original**: 10 हो पगधनरेहसे पराजित हो जायगी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10635)
- **Original**: और यदि प्रथम मगधनरेशसे छड़ते हैं तो तससे क्षोण हुई यादवसेनाकों तस्माददुर्ग करिष्यामि यदूनामरिदुर्जयम्‌ । स्त्रियोउपि यत्र युद्धेयु: कि पुनर्वृष्णिपुड्ता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10636)
- **Original**: 11 बलवान्‌ कालयवन नष्ट कर दंगा। हाथ ! इस भ्रक्तार यादनॉपर [ एक ही साथ ] यह दो तरहक्ी आपति आ पहुँची है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10637)
- **Original**: अतः मैं यादबेकि लिये एक ऐसा दुर्जय मयि मत्ते प्रमत्ते वा सुप्ते प्रवसितेषपि वा। दुर्ग तैयार कराता हूँ जिसमें बैठकर वृष्णिश्रेष्ट यादवॉकी तो यादवाभिभवं दुष्टा मा कुर्बनत्बस्यो 5धिका:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10638)
- **Original**: बात ही क्या है, हियाँ भी युद्ध कर सकें
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10639)
- **Original**: उस दुर्गमें रहनेपर यदि मैं मत्त, प्रमत्त (असावधान), सोया अधवा इति सकित्त्य गोविन्दो योजनानां महोदधिम्‌ । कहीं बाहर भी गया होऊँ तब भी, अधिक-से-अधिक दुष्ट ययाचे द्वादश पुरी द्वारकां तत्र निर्ममे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10640)
- **Original**: 13 पहोद्यानां महावप्रों तटाकशतशोभिताम्‌। प्रासादगृहसम्बाधामिद्धस्थेत्ाममावतीम्‌ू_
- **Translation**: 

---

