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

### Verse 1 (Vaivtpuran 543.16514)
- **Original**: हूँ। नरेश्वर! दुर्बल एवं योगी जरासंधको युद्धमें प्रफुल्लित हो उठा। उन्होंने वेगपूर्वक उठकर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16515)
- **Original**: जीतकर श्रीकृष्णको अहंकार हो गया है। वे अपने शतानन्दजीका आलिड्रन किया। उस समय
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16516)
- **Original**: मन अपनेको वीर मानने लगे हैं; परंतु यदि वे राजाके मुखपर प्रसन्नता खेल रही थी; उन्होंने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16517)
- **Original**: विवाह करनेकी इच्छासे मेरे नगरमें आयेंगे तो शतानन्दजीको नाना प्रकारके रत्न, सुवर्ण, वस्त्र,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16518)
- **Original**: मैं क्षणभरमें निश्चय ही उन्हें यमलोक पहुँचा दूँगा।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16519)
- **Original**: 726 + संक्षिप्त श्रह्मैधर्तपुराण « 44% %# 4 %# 6 ############### ## ###### 6 # ##### 66 ##### ##### 4 5 जो वैश्यजातीय नन्दका पुत्र, गौओंका चरवाहा,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16520)
- **Original**: पूर्णरूपसे सलाह को। तत्पश्चात्‌ जो सबको अभीष्ट गोपाड्ुनाओंका लम्पट और ग्वालोंकी जूँठन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16521)
- **Original**: था, ऐसा शुभ लग्न निश्चित करके एक योग्य एवं खानेवाला है, उसे आप कन्या देना स्वीकार करते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16522)
- **Original**: अन्तस्प्ज ब्राह्मणको द्वारका भेजनेकी व्यवस्था की। हैं। यह महान्‌ आश्चर्यकों बात है! राजेन्द्र! इस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16523)
- **Original**: इधर राजा तुरंत ही हर्षपूर्वक सामग्री जुटानेमें लग बकवादीके वचनसे आपकी बुद्धि मारी गयी है; गये और पुत्रके कहनेसे उन्होंने चारों ओर इसी कारण इस भिक्षुक ब्राह्मणके कहनेसे आप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16524)
- **Original**: निमन्त्रण-पत्र भेज दिये। उधर उस ब्राह्मणने देवयोग्या रुक्मिणीको श्रीकृष्णके हाथों सौंपना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16525)
- **Original**: सुधर्मा-सभामें, जो राजाओं तथा देबताओंसे चाहते हैं। अरे! वह तो न राजपुत्र है, न शूरवीर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16526)
- **Original**: परिवेष्टित थी; पहुँचकर राजा उग्रसेनकों वह है, न कुलीन है, न पवित्र आचरणवाला है,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16527)
- **Original**: मज़जल-पत्रिका दी। उस परम माज्लिक पत्रको न दाता है, न धनी है, न योग्य है और न
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16528)
- **Original**: सुनकर राजा उग्रसेनका मुख प्रफुल्लित हो उठा। जितेद्धिय ही है। इसलिये भूपाल! आप शिशुपालको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16529)
- **Original**: उन्होंने हर्षमें भरकर ब्राह्मणोंको हजारों स्वर्णमुद्राएँ कन्या दीजिये; क्योंकि वह सुपूत एवं राजाधिराजका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16530)
- **Original**: दान कीं और द्वारकामें चारों ओर दुन्दुभिका शब्द पुत्र है तथा अपने बलसे रुद्रकों भी संतुष्ट कर [कराकर घोषणा करा दी। श्रीकृष्णकी उस बारातमें चुका है। राजन्‌! अब शीघ्र ही पत्र भेजकर बड़े-बड़े देवता, मुनि, राजागण, यादवगण, कौरव, विभिन्न देशोंमें उत्पन्न हुए नरेशों, भाई-बन्धुओं पाण्डब, विद्वान्‌ ब्राह्मण, माली, शिल्पी, गायक, तथा मुनिवरोंको निमन्त्रित कौजिये।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16531)
- **Original**: गन्धर्व आदि सम्मिलित हुए। उस समय उपबर्हण तदनन्तर रुक्मिकौ बात सुनकर पुरोहितसहित
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16532)
- **Original**: नामक गन्धर्वके रूपमें तुम नारद भी बारातके राजेन्द्र भीष्मकने एकान्त स्थानमें मन्त्रीके साथ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16533)
- **Original**: साथ थे। (अध्याय 105) 2501-40 /0+> 0 रेबती और बलरामके विवाहका वर्णन तथा रुक्‍्मी, शाल्व, शिशुपाल और दन्तवकरका श्रीकृष्णको कटुबचन कहना श्रीनारायण कहते हैं--नारद! इसी समय
- **Translation**: 

---

