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

### Verse 1 (Vaivtpuran 67.6155)
- **Original**: विष्णुका स्तवन सम्पूर्ण सम्पत्तियोंकी वृद्धि यज्ञमें शिवजीकी निन्‍दा होनेके कारण मैंने उस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.6156)
- **Original**: करनेवाला, सुखदायक, मोक्षप्रद, साररूप, स्वामीके शरीरका परित्याग कर दिया। फिर मैंने ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.6157)
- **Original**: सौभाग्यका वर्धक, सम्पूर्ण सौन्दर्यका बीज, शैलराजके कर्मोंके परिणामस्वरूप हिमालयकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.6158)
- **Original**: यशकी राशिकों बढ़ानेवाला, हरि-भक्तिका दाता पत्नीके गर्भसे जन्म धारण किया। इस जन्ममें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.6159)
- **Original**: और तत्त्वज्ञान तथा बुद्धिकी विशेषरूपसे उन्नति भी अनेक प्रकारकी तपस्याके फलस्वरूप शिवजी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6160)
- **Original**: करनेवाला है।* मुझे प्राप्त हुए और ब्रह्माजीकी प्रार्थनासे उन (अध्याय 7) निक,.. अ] क्र पार्वत्युवाच-- कृष्ण जानासि मां भद्र नाह॑ त्वां ज्ञातुमीश्ववी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6161)
- **Original**: के बा जानन्ति बेदज्ञा वेदा वा वेदकारका:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6162)
- **Original**: त्वद॑शास्त्वां न जानन्ति कर्थ ज्ञास्यन्ति त्वत्कला:। त्व॑ चापि तत्व॑ जानासि किमन्ये ज्ञातुमीश्वरा:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6163)
- **Original**: सूक्ष्मात्‌ सूक्ष्मतमो5व्यक्त: स्थूलात्‌ स्थूलतमो महान्‌ । विश्वस्त्व॑ विश्वरूपक्ष विश्वबीर्ज सनातन:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6164)
- **Original**: कारण त्वं च कारणानां च कारणम्‌। तेज:स्वरूपो भगवान्‌. निराकारों. निराश्रय:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6165)
- **Original**: निर्लिप्तो निर्ुण: साक्षी स्वात्मारामः परात्पर:। प्रकृतेशो विराइबीज विराड्रूपस्त्वमेव च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6166)
- **Original**: सगुणस्त्वं प्राकृतिक: कलया सृष्टिहेतवे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6167)
- **Original**: पुमांस्त्य॑च वेदान्यों नक्‍्वचिद्‌ भवेत्‌ । जीवस्त्व॑ साक्षिणों भोगी स्वात्मन: प्रतिबिम्बका:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6168)
- **Original**: कर्म त्वं कर्मंबीज॑ त्व॑ कर्मणां फलदायक: । ध्यायन्ति योगिनस्तेजस्त्थदीयमशरीरिणम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6169)
- **Original**: केचिच्चतुर्भुजं शान्त॑ लक्ष्मीकान्त मनोहरम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.18053)
- **Original**: 796 के संज्षिप्त ब्रह्मवैवर्तपुराण न 040
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.18054)
- **Original**: ] 3))0024440]08]4 2 44)7/]]/444]4] मन्त्र: षड़क्षरोई्यं च भक्तानां कल्पपादप:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.18055)
- **Original**: विचारों नास्ति बेदेषु ग्रहणे च मनोर्मुने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.18056)
- **Original**: मन्त्ग्रहणमात्रेण. विष्णुतुल्यो. भवेन्नरः । मम बकक्‍त्रं सदा पातु 0 दुर्गाये नमोउन्तत:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.18057)
- **Original**: 39 दुर्गे रक्ष इृति च्र कण्ठं पातु सदा मम । 30 हीं श्रीमिति मन्त्रो5यं स्कन्ध॑ पातु निरन्तरम्‌
- **Translation**: 

---

