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

### Verse 1 (Vaivtpuran 32.18527)
- **Original**: इति औब्रह्मवैवर्ते परज़ुरामं प्रति शिवेनोपदिषं श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (गणपत्तिखण्ड 32। 27--74) आह 8#फसफ 4 980000080 बअहादिकृत:ः श्रीकृष्णस्तवराज: नत्वा तेज:स्वरूप॑ च तमीशं अत्रिदशेश्वरा: । तब्रोत्थाय ध्यानयुक्ता: प्रतस्थुस्तेजस: पुर:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.18528)
- **Original**: ध्यात्वैव जगतां धाता त्रभूव सम्पुटाझ्ञलि: । दक्षिणे शंकरं कृत्वा वामे धर्म च॒ नारद
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.18529)
- **Original**: भक्त्युद्रेकात्‌ प्रतुष्ठाव ध्यानैकतानमानस: । परात्परं_ गुणातीतं परमात्मानमी श्वरम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.18530)
- **Original**: ब्रह्मोवाच बरं बरेण्यं बरद॑ वरदानां च कारणम्‌ । कारणं सर्वभूतानां तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.18531)
- **Original**: मड़ल्य॑ मड्लाहँ च॒ मड़ल॑ मड्ुलप्रदम्‌ । समस्तमड्गलाधारं तेजोरूपं॑ नमाम्बहम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.18532)
- **Original**: स्थित सर्वत्र निर्लिप्तमात्मरूपं॑ परात्यरम्‌ । निरीहमवितक्य॑ च तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.18533)
- **Original**: सगुणं निर्गुणं ब्रह्म ज्योतीरूपं सनातनम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.18534)
- **Original**: साकारं च निराकारं तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.18535)
- **Original**: तमनिर्वचनीय॑ च व्यक्तमय्यक्तमेककम्‌ । स्वेच्छामयं सर्वरूपं॑ तेजोरूप॑. नमाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.18536)
- **Original**: गुणत्रयविभागाय रूपत्रयधरं परम्‌। कलया ते सुरा: सर्वे कि जानन्ति भ्रुतेः परम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.18537)
- **Original**: सर्वाधारं सर्वरूप॑ सर्वबीजमबीजकम्‌ । सर्वान्तकमनन्त॑ च्॒ तेजोरूपं॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.18538)
- **Original**: लक्ष्य यद्‌ गुणरूपं च् वर्णनीयं विचक्षणै: । कि. वर्णयाम्यलक्ष्य॑ते तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.18539)
- **Original**: अशरीर विग्रहवदिन्द्रियवदतीन्द्रियम्‌ । यदसाक्षि सर्वसाक्षि तेजोरूपं नमाम्यहम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7775)
- **Original**: 370 + संक्षिप्त ब्रह्मचैचर्तपुराण ] ऋऋकऋ%%ऋ%%############# ###%%$%%%%#%%ऋ#ऋ 54% #######&#&###&##%##%##%ऊ$कऊकऋकऊकऋकऊकककऋऊऋककककऊकक साथ सती हो गयी। भूपाल! इन दोनोंके वधसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7776)
- **Original**: असत्को कहनेमें समर्थ ये सारे नरेश भी परलोकमें तुम्हारी क्या गति होगी? यह सारा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7777)
- **Original**: श्रवण करें; क्योंकि समदृष्टि रखनेवाले सत्पुरुष संसार तो कमलके पत्तेपर पड़े हुए जलकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7778)
- **Original**: लोग पक्षपातकी बात नहीं कहते। युद्धस्थलमें बूँदकी तरह मिथ्या ही है। सुयश हो अथवा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7779)
- **Original**: इतना कहकर परशुराम चुप हो गये। तब अपयश, इसकी तो कथामात्र अवशिष्ट रह जाती
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7780)
- **Original**: बृहस्पतिके समान बुद्धिमानू राजाने कहना है। अहो ! सत्पुरुषोंकी दुष्कीर्ति हो, इससे बढ़कर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7781)
- **Original**: आरम्भ किया। और क्या विडम्बना होगी? कपिला कहाँ गयी,, .कार्तवीर्यार्जुनने कहा--हे राम! आप तुम कहाँ गये, विवाद कहाँ गया और मुनि श्रीहरिके अंश, हरिके भक्त और जितेन्द्रिय हैं। कहाँ चले गये; परंतु एक विद्वान्‌ राजाने जो
- **Translation**: 

---

