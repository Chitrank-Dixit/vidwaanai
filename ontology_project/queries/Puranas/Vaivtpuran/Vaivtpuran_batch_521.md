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

### Verse 1 (Vaivtpuran 31.7591)
- **Original**: धर्म कल्याणबीजानां येदानां सामवेदक: । धर्माणां सत्यरूपों यो विशिष्ट. त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7592)
- **Original**: जले शैत्यस्वरूपो यो गन्धरूपश्च॒ भूमिषु । शब्दरूपश्च॒गगने त॑ प्रणम्यं नमाम्यहम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.19130)
- **Original**: * श्रीकृष्णस्तोत्राणि * 833 #%##%#%%$%%##%%#%$%#%##%#%%### ###%%%## ############ ####%#################%#####%&#% ##ऋ #ऋ% यदि स्यात्‌ सिद्धकवचो जीवन्मुक्तो भवेत्तु सः । निश्चितं कोटिवर्षाणां पूजाया: फलमाप्रुयात्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.19131)
- **Original**: राजसूयसहस्राणि बाजपेयशतानि... च। अश्रप्ेधायुतान्येव नरमेधायुतानि च
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.19132)
- **Original**: महादानानि यान्येव प्रादक्षिण्यं भुवस्तथा । त्रैलोक्यविजयस्यास्य कलां नाहन्ति घोड़शीम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.19133)
- **Original**: ब्रतोपवासनियमा: स्वाध्यायोउध्ययनं॑ तपः । स्तान॑ च॒ सर्वतीर्थेषु नास्याईन्ति कलामपि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.19134)
- **Original**: सिद्धत्वममरत्व॑ च दासत्व॑ श्रीह्रेरपि । यदि स्यात्‌ सिद्धकबच: सर्ब प्राप्रोति निश्चितम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.19135)
- **Original**: स भवेत्‌ सिद्धकबचो दशलक्षं जपेत्तु यः। यो भवेत्‌ सिद्धकबच: सर्वज्ञ: स भवेद्‌ श्रुवम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.19136)
- **Original**: इृदं कबचमज्ञात्वा भजेत्‌ कृष्ण सुमन्दधी: । कोटिकल्पप्रजप्तोतपि न मन्त्र: सिर्द्धिदायकः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.19137)
- **Original**: गृहीत्वा कवच वत्स महीं निःक्षत्रियां कुरु । त्रिःसप्तकृत्तो निःशद्भ: सदानन्दोइवलीलया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.19138)
- **Original**: राज्यं देयं शिरो देयं प्राणा देयाश्व पुत्रक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.19139)
- **Original**: एवं भूत॑ च कवच न देय॑ प्राणसड्डूटे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.19140)
- **Original**: इति श्रीब्रह्मवैकतें त्रैलोक्यविजयं वाम श्रीकृष्णकवर्च॑ सम्पूर्णम्‌। (गणपतिखण्ड 31। 23--57) बरह्माणं प्रति योगनिद्रयोपदिष्ठट॑ श्रीकृष्णकवचम्‌ योगनिद्रोवाच दूरीभूत कुरु भयं भय किं ते हरौ स्थिते । स्थितायां मयि चर ब्रह्मन्‌ सुखं तिप्ठ जगत्पते
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.19141)
- **Original**: श्रीहरिः पातु ते बकत्रं मस्तक मधुसूदन: । श्रीकृष्णश्रक्षुषी पातु नासिकां राधिकापति:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.19142)
- **Original**: कर्णयुग्मं च कण्ठं च कपाल॑ पातु माधव:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.19143)
- **Original**: कपोल॑ पातु गोविन्द: केशांश्व केशव: स्वयम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.19144)
- **Original**: अधथरीौष्ठ॑ इृषीकेशो दन्तपंक्तिं गदाग्रजः । रासेश्वशश्न रसनां तालुक॑ वामनो विभु:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.19145)
- **Original**: वक्ष: पातु मुकुन्दस्ते जठरं पातु दैत्यहा । जनार्दनः पातु नाभिं पातु विष्णुश्न ते हनुम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.19146)
- **Original**: नितम्बयुग्म॑ गुहां चर पातु ते पुरुषोत्तम: । जानुयुग्म॑ं जानकीशः पातु ते सर्वदा विभु:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.19147)
- **Original**: हस्तयुग्म॑ नृसिहश्ष॒पातु सर्वत्र सड्डटे । पादयुग्म॑ वराहश्च॒ पातु॒ ते कमलोद्धव:
- **Translation**: 

---

