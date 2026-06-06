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

### Verse 1 (Vaivtpuran 46.4574)
- **Original**: नहीं हो सकता। यदि यह स्तोत्र सिद्ध हो जाय तो गोलोकसे सुरभी गौ आयी और उसने अपने दूधसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 46.4575)
- **Original**: पुरुषके लिये विष भी अमृत-तुल्य हो जाता है। आदरणीया मनसाको स्नान कराकर सादर उनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 46.4576)
- **Original**: इस स्तोत्रका पाँच लाख जप करनेपर यह सिद्ध पूजन किया। साथ ही, उसने सर्वदुर्लभ गोप्य हो जाता है। फिर मन्त्रसिद्ध पुरुष सर्पशायी तथा ज्ञानना भी उपदेश दिया। उस समय सुरभी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 46.4577)
- **Original**: सर्पवाहन हो सकता है अर्थात्‌ उसपर्‌ सर्पका कोई देवताओंसे पूजित हो स्वर्गलोकमें चली गयी।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 46.4578)
- **Original**: प्रभाव नहीं पड़ सकता। (अध्याय 44-46) #<+# 6085 0क्‍न्‍5+र>> आदिगौ सुरभीदेवीका उपाख्यान नारदजीने पूछा--ब्रह्मनू! वह सुरभीदेवी कौन थी, जो गोलोकसे आयी थी? मैं उसके जन्म और चरित्र सुनना चाहता हूँ। भगवान्‌ नारायण बोले--नारद! देवी सुरभी गोलोकमें प्रकट हुई। वह गौओंकी अधिष्ठात्री देवी, गौओंकी आदि, गौओंकी जननी तथा सम्पूर्ण गौओंमें प्रमुख है। मुने! मैं सबसे पहली सृष्टिका प्रसड्र सुना रहा हूँ, जिसके अनुसार पूर्वकालमें वृन्दावनमें उस सुरभीका ही जन्म हुआ था। एक समयकी बात है। गोपाड्रनाओंसे घिरे हुए राधापति भगवान्‌ श्रीकृष्ण कौतृहलवश श्रीराधाके साथ पुण्य-बृन्दावनमें गये। वहाँ वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 46.4579)
- **Original**: विहार करने लगे। उस समय कौतुकवश उन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 46.4580)
- **Original**: अहँ. करोमि त्वां पूज्यां प्रीतिक्ष वर्धते मम । नित्यं यद्यपि त्व॑ं पूज्या भवेउत्र जगदम्बिके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 46.4581)
- **Original**: तथापि तब पूजां च वर्धयामि च॒ स्वत:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 46.4582)
- **Original**: ये त्वामाषादसंक्रान्त्यां पूजयिष्यन्ति भक्तित:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 46.4583)
- **Original**: पक्षम्यां मनसाख्यायामिषान्त॑ वा दिने दिने । पुत्रपौत्रादयस्तेषां वर्धन्ते च धनानि वै
- **Translation**: 

---

### Verse 11 (Vaivtpuran 46.4584)
- **Original**: यशस्विन: कौर्तिमन्तों विद्यावन्तों गुणान्यिता:। ये त्वां न पूजयिष्यन्ति निन्दन्त्यज्ञानतों जना:। लक्ष्मीहीना भविष्यन्ति तेषां नागभयं सदा । त्व॑ स्वर्गलक्ष्मी: स्वर्ग च वैकुण्ठे कमलाकला
- **Translation**: 

---

### Verse 12 (Vaivtpuran 46.4585)
- **Original**: नारायणांशो भगवान्‌. जरत्कारुमुनीधचर: । तपसा तेजसा त्वां च मनसा ससृजे पिता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 46.4586)
- **Original**: अस्माक॑ रक्षणायैव तेन त्व॑ मनसाभिधा । मनसा देवितुं शक्ता स्वात्मना सिद्धयोगिनी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 46.4587)
- **Original**: तेन त्वं मनसादेवी पूजिता वन्दिता भवे । ये भक्त्या मनसां देवा: पूजयन्त्यनिश भृशम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 46.4588)
- **Original**: तेन त्वां मनसादेवीं प्रवदन्ति मनौषिण: । सत्यस्वरूपा देवी त्वं शश्वत्सत्वनिषेषया
- **Translation**: 

---

### Verse 16 (Vaivtpuran 46.4589)
- **Original**: यो हि यद्‌ भावयेन्नित्य॑ शत्त॑ प्राप्रोति तत्समस्‌ । इन्द्रश मनसां स्तुत्या गृहीत्वा भगिनीं च तामू
- **Translation**: 

---

### Verse 17 (Vaivtpuran 46.4590)
- **Original**: न प्रजगाम स्वभवन॑ भूषावासपरिच्छदाम्‌ । (प्रकृतिखण्ड 46
- **Translation**: 

---

### Verse 18 (Vaivtpuran 46.4591)
- **Original**: । 128-1422)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 46.4592)
- **Original**: क का 247 #%#######%ऋ########%$# 55% %%$#%%$##$4%$######%#######&######55 कक ##%##8# स्वेच्छामय प्रभुके मनमें सहसा दूध पीनेकी इच्छा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 46.4593)
- **Original**: षडक्षर-मन्त्र है। एक लाख जप करनेपर मन्त्र जाग उठी। तब भगवान्‌ने अपने वामपार्श्से
- **Translation**: 

---

