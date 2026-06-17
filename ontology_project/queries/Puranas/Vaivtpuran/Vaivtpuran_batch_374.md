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

### Verse 1 (Vaivtpuran 18.1199)
- **Original**: तुम सब लोग मां महेशं च धर्म व भक्त च भक्तवत्सल। मेरे बरसे तपस्याके फलदाता हो जाओ। त्वप्प्रसादेन पुत्रेभ्यों दास्यामि भक्तिसंयुत:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1200)
- **Original**: ब्रह्मण्डपावनस्थास्थ कवचस्य हरिः स्वयम्‌। ख्रह्मजी बोले--महाभाग! राधावललभ!
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1201)
- **Original**: ऋषिशठन्दश्न गायत्री देवो5ह॑ जगदीश्वरः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1202)
- **Original**: प्रभो! ब्रह्माण्डपावन नामक जो कवच आपने धर्मार्थकाममोक्षेषु विनियोग: प्रकीर्तित:। प्रकाशित किया है, उसका उपदेश कृपापूर्वक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1203)
- **Original**: त्रिलक्षबारपठनात्‌ सिद्धिदं कवच विशे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1204)
- **Original**: मुझको, महादेवजीको तथा धर्मकों दीजिये। इस ब्रह्माण्डपावन कवचके स्वयं श्रीहरि भक्तवत्सल! हम तीनों आपके भक्त हैं। आपकी ऋषि हैं, गायत्री छन्द हैं, मैं जगदीश्वर श्रीकृष्ण कृपासे मैं अपने पुत्रोंकों भक्तिपूर्वक इसका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1205)
- **Original**: ही देवता हूँ तथा धर्म, अर्थ, काम और मोक्षकी उपदेश दूँगा। सिद्धिके लिये इसका विनियोग* कहा गया है। श्रीकृष्ण उवाच
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1206)
- **Original**: बिधे! तोन लाख बार पाठ करनेपर यह कबच श्रृणु वक्ष्यामि ब्रह्मेश धर्मेंदं कवच परम्‌।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1207)
- **Original**: सिद्धिदायक होता है। अहं दास्थामि युध्मभ्य॑ गोपनीयं सुदुर्लभम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1208)
- **Original**: यो भबेत्‌ सिद्धकवचो मम तुल्यो भवेत्तु सः। यस्मै कस्मै न दातव्य॑ प्राणतुल्य॑ ममैव हि। तेजसा सिद्धियोगेन ज्ञानेन विक्रमेण च
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1209)
- **Original**: यत्तेजो मम देहेउस्ति तत्तेज: कबचेठपि च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1210)
- **Original**: प्रणवों मे शिरः पातु नमो रासेश्वराय च। श्रीकृष्णने कहा--ब्रह्मन्‌! महेश्वर! और भालं पायाज्नेत्रयुग्पं नमो राधेश्वराय च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1211)
- **Original**: धर्म! तुम लोग सुनो! मैं इस उत्तम कवचका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1212)
- **Original**: कृष्ण: पायाच्छेत्रयुग्मं हे हरे प्राणमेव च। वर्णन कर रहा हूँ। यद्यपि यह परम दुर्लभ और जिड्लिकां वहिजाया वर्णन कर रहा हूँ। यद्यपि यह परम दुर्लभ और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1213)
- **Original**: जिद्लिकां वहिजाया तु कृष्णायेति च सर्वतः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1214)
- **Original**: + इस कवचका विनियोगवाक्य संस्कृतमें इस प्रकार है-- 35 अस्य श्रीब्रह्माण्डपावनकवचस्य साक्षात्‌ श्रीहरि: ऋषि:, गायत्री छन्द:, सं एवं जगदी श्वर: श्रीकृष्णो देवता धर्मार्धकाममोक्षेपु विनियोग:।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1215)
- **Original**: » ग्रह्मतण्ड + 64488 0 640 ]04 09498 4 6226 4 2 6 6 6 6 6 6 3
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1216)
- **Original**: 3 4 0 6
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1217)
- **Original**: श्रीकृष्णाय स्वाहेति च कणठं पातु षडक्षर:। रक्षा करे। '40 नमो भगवते रासमण्डलेशाय हीं कृष्णाय नमो वक्त्र॑ क्लीं पूर्व श्च॒ भुजद्दयम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1218)
- **Original**: स्वाहा ' (रासमण्डलके स्वामी सच्चिदानन्दस्वरूप नमो गोपाड्ुनेशाय स्कन्धावष्टाक्षरो उयतु। भगवान्‌ श्रीकृष्णको नमस्कार है। उनकी प्रसन्नताके दन्तपंक्तिमोष्ठयुग्म॑ नमो गोपीश्वराय च
- **Translation**: 

---

