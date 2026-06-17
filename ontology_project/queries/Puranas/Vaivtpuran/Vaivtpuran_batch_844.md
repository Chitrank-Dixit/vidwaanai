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

### Verse 1 (Vaivtpuran 543.15194)
- **Original**: खानेबाला मनुष्य भविष्यमें अवश्य ही राजा होता है, नग्र है और बाल खोले हुए है, उसे अपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15195)
- **Original**: है। छत्र, पादुका और निर्मल एवं तीखे खड्गकी देखे हुए स्वप्रका कोई फल नहीं मिलता। निद्रालु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15196)
- **Original**: प्राप्ति धान्य-लाभकी सूचना देती है। खेल-खेलमें मनुष्य स्वप्न देखकर यदि पुनः नींद लेने लग
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15197)
- **Original**: ही पानीके ऊपर तैरनेवाला मनुष्य प्रधान होता जाता है अथवा मूढ़तावश रातमें ही किसी दूसरेसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15198)
- **Original**: है। फलवान्‌ वृक्षका दर्शन और सर्पका दंशन कह देता है; तब उसे उस स्वप्रका फल नहीं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15199)
- **Original**: धन-प्राप्तिका सूचक है। स्वप्रमें सूर्य और मिलता। किसी नीच पुरुषसे, शत्रुसे, मूर्ख
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15200)
- **Original**: चन्द्रमाके दर्शनसे रोग दूर होता है। घोड़ी, मुर्गी मनुष्यसे, स्त्रीसे अथवा रातमें ही किसो दूसरेसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15201)
- **Original**: और क्रौ्ीको देखनेसे भार्याका लाभ होता है।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15202)
- **Original**: 660 * संक्षिप्त ग्रह्मवैवर्तपुराण « %%#$%$##########&##########6##&###&########
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15203)
- **Original**: 68, 64 #8### #%% 5 क#&##4 कक %%%ऋ#क स्वप्रमें जिसके पैरोंमें बेड़ी पड़ गयी, उसे प्रतिष्ठा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15204)
- **Original**: हो मुस्कराते हुए स्वप्रमें जिसको कोई फल दें, और पुत्रकों प्राप्ति होती हैं। जो सपनेमें नदीके किनारे नये अथवा फटे-पुराने कमलके पत्तेपर दही मिला हुआ अन्न और खीर खाता है; वह भविष्यमें राजा होता है। जलौका (जोंक), बिच्छू और साँप यदि स्वप्रमें दिखायी दें तो धन, पुत्र, विजय एवं प्रतिष्ठाकी प्राप्ति होती है। सींग और बड़ी-बड़ी दाढ़वाले पशुओं, सूअरों और वबानरोंसे यदि स्वप्रमें पीडा प्राप्त हो तो मनुष्य निश्चय ही राजा होता और प्रचुर धन-राशि प्राप्त कर लेता है। जो स्वप्में मत्स्य, मांस, मोती, शड्ख, चन्दन,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15205)
- **Original**: उसे पुत्र होता है। पिताजी ! ब्राह्मण स्वप्रमें जिसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15206)
- **Original**: शुभाशीर्वाद देते हैं, उसे अवश्य ऐश्वर्य प्राप्त होता 'है। सपनेमें संतुष्ट ब्राह्मण जिसके घर आ जाय;
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15207)
- **Original**: उसके यहाँ नारायण, शिव और नब्रह्माका प्रवेश
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15208)
- **Original**: होता है; उसे सम्पत्ति, महान्‌ सुयश, पग-पगपर सुख, सम्मान और गौरवकी प्राप्ति होती है। यदि स्वप्रमें अकस्मात्‌ गौ मिल जाय तो भूमि और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15209)
- **Original**: पतिव्रता स्त्री प्राप्त होती है। स्वप्रमें जिस पुरुषको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15210)
- **Original**: हाथी सूँड्से उठाकर अपने माथेपर बिठा ले;
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15211)
- **Original**: उसे निश्चय ही राज्य-लाभ होगा। स्वप्रमें संतुष्ट होरा, शराब, खून, सुवर्ण, विष्ठा तथा फले-फूले
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15212)
- **Original**: ब्राह्मण जिसे इृदयसे लगाये और फूल हाथमें बेल और आमको देखता है; उसे धन मिलता
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15213)
- **Original**: दे; वह निश्चय ही सम्पत्तिशाली, विजयी, यशस्वी है। प्रतिमा और शिवलिज्जके दर्शनसे विजय और
- **Translation**: 

---

