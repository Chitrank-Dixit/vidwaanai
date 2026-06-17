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

### Verse 1 (Nard Puran 0.1321)
- **Original**: सिद्ध शब्दोंका हो लिप, लुप्‌, बप्‌, शप्‌, स्वंफू सृप्‌, यभ, रभू, लभ्‌,
- **Translation**: 

---

### Verse 2 (Nard Puran 0.1322)
- **Original**: प्रकृति, प्रत्यय, आदेश और आगम आदिके द्वारा गम, नम, यम्‌, रम, क्रुशदंशू, दिशू, दृशू, मृश्‌,
- **Translation**: 

---

### Verse 3 (Nard Puran 0.1323)
- **Original**: लघुमार्गसे सम्यक्‌ निरूपण किया जाता है। इस रिशू, रुशू, लिश, विशू
- **Translation**: 

---

### Verse 4 (Nard Puran 0.1324)
- **Original**: स्पृशू, कृष्‌
- **Translation**: 

---

### Verse 5 (Nard Puran 0.1325)
- **Original**: प्रकार तुमसे निरुक्तका यत्किंचित्‌ ही वर्णन किया त्विष्‌, तुष्‌, द्विष, दुष्‌, पुष्ठ, पिष, विष, शिष्‌,
- **Translation**: 

---

### Verse 6 (Nard Puran 0.1326)
- **Original**: गया है। नारद! इसका पूर्णरूपसे बर्णन तो कोई भी शुष्‌, श्लिषू, घसू, वस्‌, दह; द्विह, दुहद, नह, मिह,
- **Translation**: 

---

### Verse 7 (Nard Puran 0.1327)
- **Original**: कर ही नहीं सकता
- **Translation**: 

---

### Verse 8 (Nard Puran 0.1328)
- **Original**: 86--88
- **Translation**: 

---

### Verse 9 (Nard Puran 0.1329)
- **Original**: (पूर्वभाग द्वितीयपाद रुह, लिह तथा वह्‌
- **Translation**: 

---

### Verse 10 (Nard Puran 0.1330)
- **Original**: ये. हलन्तोंमें एक सौ
- **Translation**: 

---

### Verse 11 (Nard Puran 0.1331)
- **Original**: अध्याय 53) #ज7“>सिड420020 त्रिस्कन्ध ज्यौतिषके वर्णन-प्रसडूमें गण्िगतविषयका प्रतिपादन सननन्‍्दन उबाच साक्षात्‌ ब्रह्माजोने उपदेश किया है तथा जिसके ज्यौतिषाडुं प्रवक्ष्यामि यदुक्त ब्रह्मणा पुरा। विज्ञानमात्रसे मनुष्योंके धर्मकी सिद्धि हो सकती अस्थ विज्ञानमात्रेण धर्मसिद्धिर्भवेश्रणाम्‌
- **Translation**: 

---

### Verse 12 (Nard Puran 0.1332)
- **Original**: ब्रह्मन्‌! ज्यौतिषशास्त्र चार लाख श्लोकोंका त्रिस्कन्ध॑ ज्यौतिषं शास्त्र चतुर्लक्षपुदाइतम्‌।
- **Translation**: 

---

### Verse 13 (Nard Puran 0.1333)
- **Original**: बताया गया है। उसके तीन' स्कन्थ हैं, जिनके नाम गणित जातकं विप्र संहितास्कन्थेसंज्ञितम्‌
- **Translation**: 

---

### Verse 14 (Nard Puran 0.1334)
- **Original**: ये हैं-गणित (सिद्धान्त), जातक (होरा) और गणिते परिकर्माणि खगमध्यस्फुटक्रिये।
- **Translation**: 

---

### Verse 15 (Nard Puran 0.1335)
- **Original**: संहिता
- **Translation**: 

---

### Verse 16 (Nard Puran 0.1336)
- **Original**: गणितमें परिकर्म.', ग्रहोंके मध्यम एवं अनुयोगश्वन्धसूर्यग्रहणं॑ चोदयास्तकम्‌
- **Translation**: 

---

### Verse 17 (Nard Puran 0.1337)
- **Original**: स्पष्ट करनेकी रीतियाँ बतायी गयी हैं। इसके सिवा छाया श्रृड्रोन्नतियुती पातसाधनमीरितम्‌। अनुयोग (देश, दिशा और कालका ज्ञान), चन्द्रग्रहण, श्रीसनन्दनजी कहते हैं--देवर्षे ! अंब मैं ज्यौतिष
- **Translation**: 

---

### Verse 18 (Nard Puran 0.1338)
- **Original**: सूर्यग्रहण, उदय, अस्त, छायाधिकार, चन्द्र-श्वड्जोन्नति', नामक वेदाड्रका वर्णन करूँगा, जिसका पूर्वकालमें
- **Translation**: 

---

### Verse 19 (Nard Puran 0.1339)
- **Original**: ग्रहयुति (ग्रहोंका योग) तथा पात (महापांत*सूर्य- 3. किसी-किसीके मतसे ज्यौतिषके पाँच स्कन्ध हैं-सिद्धान्त, होरा, संहिता, स्वर और सामुद्रिक। सिद्धान्तको ही गणित कहते हैं। होगका ही दूसरा नाम जातक है। 2. योग, अन्तर, गुणन, भजन, वर्ग, वर्गंपूल, घन और घतसूल--ये परिकर्म कहे गये हैं। 3. द्वितीयाको जो चन्द्रोदय होता है, उसमें कभी चन्द्रमाका दक्षिण सोंग और कभी उत्तर सींग (नोक) ऊपरको उठा रहता है, उसोको 'चद्धश्ृृज्ञोत्रति' कहा गया है। ज्यौतिषमें उसके परिणामका विचार किया गया है।
- **Translation**: 

---

### Verse 20 (Nard Puran 0.1340)
- **Original**: रेडर चन्द्रमाके क्रान्तिसाम्य)-का साधन-प्रकार कहा गया है
- **Translation**: 

---

