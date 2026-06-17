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

### Verse 1 (Vaivtpuran 18.1179)
- **Original**: उपदेश किया था--यह आप बतानेकी कृपा करें। “>छ्ह्ल्न।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1180)
- **Original**: पूर्वालमें बसिष्ठजीने गन्धर्वराजको भगवान्‌ शिवके जिस द्वादशाक्षर-मन्त्र और कवच आदिका उपदेश दिया था, वह भी मुझे बताइये। यह सब सुननेके लिये मेरे मनमें बड़ा कौतूहल है क्योंकि शंकरका स्तोत्र, कवच और मन्त्र दुर्गतिका नाश करनेवाला है। सौति बोले--शौनकजी! मालतोीने जिस स्तोत्रके द्वारा परमेश्वर श्रीकृष्णणा स्तबन किया था, वहीं स्तोत्र वसिष्ठजीने उन गन्धर्व-दम्पतिको दिया था। अब उनके दिये हुए मन्त्र और कवचका वर्णन सुनिये। '34 नम्तो भगवते रासमण्डलेशाय स्वाहा' -यह षोडशाक्षर-मन्त्र उपासकोंके लिये कल्पवृक्ष-स्वरूप है। इसीका उपदेश वसिष्ठजीने था। इसी तरह शंकरजीका स्तोत्र और कवच
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1181)
- **Original**: दिया था। पूर्वकालमें श्रीहरिके पुष्करधाममें भी गन्धर्वको भूल गया था। कृपानिधान बसिष्ठने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1182)
- **Original**: ब्रह्माजीने कुमारकों यह मन्त्र दिया था तथा एकान्तमें गन्धर्वगाजकों उसका भी बोध कराया।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1183)
- **Original**: श्रीकृष्णने गोलोकमें भगवान्‌ शंकरको इसका ज्ञान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1184)
- **Original**: 56 « संक्षिप्त ब्रह्मवैयर्तपुराण « &##4&8#&& 86646 6# 8 8884 ##8# 488 # 8 ## 6 8 #$$ #/ ## ## # 5 58 55 5 5 54 55 5 555 5 56545 5 4554 % $ 5 58 888 प्रदान किया था। यहाँ भगवान्‌ विष्णुके वेदवर्णित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1185)
- **Original**: गोपनीय है तथापि तुम्हें इसका उपदेश दूँगा। स्वरूपका ध्यान किया जाता है, जो सनातन एबं
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1186)
- **Original**: परंतु ध्यान रहे, जिस-किसीको भी इसका उपदेश सबके लिये परम दुर्लभ है। पूर्वोक्त मूल मन्त्रसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1187)
- **Original**: नहीं देना चाहिये; क्योंकि यह मेरे लिये प्राणोंके उत्तम नैवेद्य आदि सभी उपचार समर्पित करने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1188)
- **Original**: समान है। जो तेज मेरे शरीरमें है, वही इस चाहिये। भगवानूका जो कवच है, वह अत्यन्त
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1189)
- **Original**: कबचमें भी है। गुप्त है। उसे मैंने अपने पिताजीके मुखसे सुना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1190)
- **Original**: कुरु सृष्टिमिमं धृत्वा धाता त्रिजगतां भव। था। विप्रवर! पूर्वकालमें त्रिशुलधारी भगवान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1191)
- **Original**: संहर्त्ता भव हे शम्भो मम तुल्यो भवे भव
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1192)
- **Original**: शंकरने ही पिताजीकों गज्भाके तटपर इसका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1193)
- **Original**: हे धर्म त्वपिपं धृत्वा भव साक्षी च कर्मणाम््‌। उपदेश दिया था। भगवान्‌ शंकरको, ब्रह्माजीको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1194)
- **Original**: तपसां फलदाता च यूयं भवत मद्दरात्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1195)
- **Original**: तथा धर्मको गोलोकके रासमण्डलमें गोपीवल्लभ ब्रह्मन्‌! तुम इस कबचको धारण करके सृष्टि श्रीकृष्णने कृपापूर्वक यह परम अद्भुत कबच
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1196)
- **Original**: करो और तीनों लोकोंके विधाताके पदपर प्रतिष्ठित प्रदान किया था। रहो। शम्भो! तुम भी इस कबचको ग्रहण करके भ्ह्मोयाच संहारका कार्य सम्पन्न करो और संसारमें मेरे समान राधाकान्त महाभाग कबचं यत्‌ प्रकाशितम्‌।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1197)
- **Original**: शक्तिशाली हो जाओ। धर्म! तुम इस कबचको ब्रह्माण्डपावन॑ नाम कृपया कथय प्रभो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1198)
- **Original**: धारण करके कर्मोंके साक्षी बने रहो
- **Translation**: 

---

