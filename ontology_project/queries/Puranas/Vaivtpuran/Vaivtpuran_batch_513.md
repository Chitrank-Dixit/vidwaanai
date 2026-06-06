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

### Verse 1 (Vaivtpuran 30.17772)
- **Original**: 786 * संक्षिप्त श्रह्मवैवर्तपुराण * असितकृतं शिवलस्तोत्रम्‌ असित उबाच जगदगुरों नमस्तुभ्यं॑ शिवाय शिवदाय च। योगीन्द्राणां च॒ योगीन्द्र गुरूणां गुरबे नप्त:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 30.17773)
- **Original**: मृत्योमु॑त्युस्वरूपेण मृत्युसंसारखण्डन । मृत्योरीश मृत्युबीज मृत्युज्षय नमोस्तु ते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 30.17774)
- **Original**: कालरूपं कलयतां कालकालेश कारण । कालादतीत कालस्य कालकाल नमोस्तु ते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 30.17775)
- **Original**: गुणातीत गुणाधार गुणबीज गुणात्मक। गुणीश गुणिनां बीज गुणिनां गुरवे नमः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 30.17776)
- **Original**: ब्रह्मस्वरूप खहाज़ ब्रह्मभावनतत्पर । ब्रह्मबीजस्वरूपेण ब्रह्मणीज नमोउस्तु ते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 30.17777)
- **Original**: इति स्तुत्वा शिवं नत्वा पुरस्तस्थौ मुनीश्चर:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 30.17778)
- **Original**: दीनवत्‌. साशुनेत्रश्ष॒ पुलकाख़ितविग्रह:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 30.17779)
- **Original**: असितेन कृतं स्तोत्र भक्तियुक्तश्न॒ यः पठेत्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 30.17780)
- **Original**: वर्षमेके हविष्याशी शंकरस्य महात्मन:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 30.17781)
- **Original**: स लभेद्‌ वैष्णावं पुत्र ज्ञानिन चिरजीविनम्‌। भवेद्धनाढ्यो दुःखी च मूको भवति पण्डित:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 30.17782)
- **Original**: अभार्यो. लभते भार्या सुशीलां च॒ पतिव्ताम्‌ । इहलोके सुखं भुक्त्वा यात्यन्ते शिवसंनिधिम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 30.17783)
- **Original**: इति श्रीब्रह्मवैवर्ते असितकृतं शिवस्तोत्रं सम्पूर्णम्‌। (श्रीकृष्णजन्मखण्ड 30
- **Translation**: 

---

### Verse 13 (Vaivtpuran 30.17784)
- **Original**: 43-51) “>> अ पथ क्‍000 हिमालयकृतं शिवस्तोत्रम्‌ (1) हिमालय उवाच त्वं ब्रह्मा सृष्टिकर्ता च त्वं विष्णु: परिपालक: । त्व॑ शिव: शिवदोउनन्त: सर्वसंहारकारक:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 30.17785)
- **Original**: त्वमीश्वरों गुणातीतों ज्योतीरूप: सनातनः । प्रकृति: प्रकृतीशश्च प्राकृतः प्रकृतेः पर:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 30.17786)
- **Original**: नानारूपविधाता त्व॑ भक्तानां ध्यानहेतवे । येषु रूपेषु यत्प्रीतिस्तत्तद्रूपं बिभर्षि च
- **Translation**: 

---

### Verse 16 (Vaivtpuran 30.17787)
- **Original**: सूर्यस्त्व॑ सृष्टिजननक आधार: सर्वतेजसाम्‌ । सोमस्त्व॑ शस्थपाता चर सतत शीतरश्मिना
- **Translation**: 

---

### Verse 17 (Vaivtpuran 30.17788)
- **Original**: वायुस्‍स्त्व॑वरुणस्त्य॑च त्वम्रग्नमि: सर्वदाहक:। मृत्युज्ञयो मृत्युपृत्यु:. कालकालो वमान्तक: । विदुषां जनकस्त्व॑ च दिद्वांश्ष विदुषां गुरु: । याक्‌ त्वं बागधिदेवी त्वं तत्कर्ता तदगुरु: स्वयम्‌। इत्येबमुक्त्वा शैलेद्रस्तस्थौ धृत्वा पदाम्बुजम्‌ । स्तोत्रमेतन्महापुण्यं. त्रिसंध्य॑ यः पठेन्नर: । अपुत्रो लभते पुत्र मासमेके पठेद्‌ यदि । चिरकालगतं॑ वस्तु लभते सहसा श्वुव॒म्‌ । कारागारे श्मशाने चर शजुग्रस्तेउतिसड्डटे । रणमध्ये महाभीते.. हिंस्नजन्तुसमन्बिते । इन्द्रस्तव॑ देवराजश्चआ॒ कालो _ मृत्युर्यमस्तथा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 30.17789)
- **Original**: खेदस्त्व॑ बवेदकर्ता चल वेदबेदाड्भपारग:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 30.17790)
- **Original**: मन्त्रस्त्व॑ हि जपस्त्यं हि तपस्त्व॑ तत्फलप्रदः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 30.17791)
- **Original**: अहो सरस्वतीबीज कस्त्यां स्तोतुमिहे धर:
- **Translation**: 

---

