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

### Verse 1 (Vaivtpuran 45.17952)
- **Original**: स्वामिभेदे पुत्रभेदे मित्रभेदे च दारुणे । स्तोत्रस्मरणमात्रेण बाडिछितार्थ लभेद्‌ श्लुवम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.17953)
- **Original**: कृत्वा इविष्यं वर्ष च् स्तोत्रराज॑ श्रूणोति या । भक्त्या दुर्गां च॒ सम्पूज्य महावन्ध्या प्रसूयते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.17954)
- **Original**: लभते सा दिव्यपुत्र ज्ञानिनं चिरजीविनमू । असौभाग्या च॑ सौभाग्यं षण्मासश्रवणाड्नभेत्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.17955)
- **Original**: नवमासं काकवन्ध्या मृतवत्सा च॑ भक्तितः । स्तोत्रराज या श्रृणोति सा पुत्र॑ लभते श्रुवम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.17956)
- **Original**: कन्यामाता पुत्रहीना पश्चमासं श्रणोति या । घटे सम्पूज्य दुर्गाँ चर सा पुत्र लभते श्लरुवम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.17957)
- **Original**: इति श्रोब्रह्मवैवर्ते परशुरामकृ्त दुगस्तोत्रं सम्पूर्णम्‌। (गणपतिखण्ड 45
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.17958)
- **Original**: 18--78 ) 42224 2 श्रीमहादेवकृतं पार्वत्या: स्तवनम्‌ श्रीमहादेव उवाच महालक्ष्मीस्वकपासि किमसाध्यं तवेश्वरि
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.17959)
- **Original**: सर्वसम्पत्स्वरूपा त्वमनन्तशक्तिरूपिणी । त्व॑ं च यस्य गृहे देवि स चैश्वर्यस्थ भाजनम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.17960)
- **Original**: न लक्ष्मीर्यदगृूहे तस्य जीवनान्मरणं वरम्‌ । अहं ब्रह्मा च विष्णुश्न त्वयि भकत्या शुभप्रदे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.17961)
- **Original**: संहारसृष्टिपाल्ये तर त्वत्प्सादाद्‌ बयं क्षमा:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.17962)
- **Original**: को बा हिमालय: कोउहं कौ कार्तिकगणेश्वरौ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.17963)
- **Original**: त्वद्विहीना ह्वाशक्ताक्ष त्ववा च वयपमीश्चरा:। इति शीब्रह्मवैवते श्रीमहादेवकुत॑ पार्वत्या: स्तवन सम्पूर्णम्‌ / ( श्रीकृष्णजन्मखण्ड 16। 129-132 न्जि ) 8300" िक:थह39070050 ब्रह्मकृतं जयदुर्गास्तोत्रम्‌ (एतदेव गोपीकृतं सर्वमड्गलस्तोत्रम्‌ ) 3 नमो जयदुर्गायै ब्रह्मोवाच दुर्गें शिवेइभये माये नारायण सनातनि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.17964)
- **Original**: जये में मड्ुलं देहि नमस्ते सर्वमड्डले
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.17965)
- **Original**: दैत्यनाशार्थतचनो. दकारः परिकीर्तित: । उकारो. विघ्ननाशार्थावाचकों. वेदसम्मत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.17966)
- **Original**: रैफो रोगप्नवचनों गश्न पापप्तवाचक: । भयजश्त्रुघ्तचनशभ्राकार: परिकीर्तित:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.17967)
- **Original**: स्मृत्युक्तिस्मरणाद यस्या एते नश्यन्ति निश्चिमम्‌ । अतो दुर्गा हरे: शक्तिईरिणा परिकीर्तिता
- **Translation**: 

---

### Verse 17 (Vaivtpuran 46.4570)
- **Original**: 246 * संक्षिप्त ब्रह्मवैयर्तपुराण * [[8[[[8[[[884777]7/244/ । 8 8
- **Translation**: 

---

### Verse 18 (Vaivtpuran 46.4571)
- **Original**: 384 8 844 04043 3 लेट देवी मनसाने अपने पुत्रके साथ पिता यह स्तोत्र पुण्यबीज कहलाता है। जो पुरुष कश्यपजीके आश्रममें दीर्घकालतक बास किया।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 46.4572)
- **Original**: मनसादेवीकी पूजा करके इस स्तोत्रका पाठ करता भ्रातृव्ग सदा उनका पूजन, अभिवादन और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 46.4573)
- **Original**: है, उसे तथा उसके बंशके लिये भी नागसे भय सम्मान करता था। ब्रह्मन्‌! तदनन्तर एक बार
- **Translation**: 

---

